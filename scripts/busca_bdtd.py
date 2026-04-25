"""
busca_bdtd.py — Coleta de teses e dissertações de repositórios brasileiros
                via protocolo OAI-PMH.

NOTA IMPORTANTE: o agregador BDTD (https://bdtd.ibict.br/vufind/OAI/Server)
estava respondendo 404 na última verificação (abr/2026). Este script usa,
por padrão, o repositório institucional **UFRGS Lume** que tem OAI-PMH
público funcional, e pode ser apontado para qualquer outro repositório
DSpace/VuFind via --endpoint.

Endpoints conhecidos que respondem (snapshot abr/2026):
    UFRGS Lume:  https://lume.ufrgs.br/oai/request          [PADRÃO]
    USP Teses:   https://teses.usp.br/oai/request
    UFMG:        https://repositorio.ufmg.br/oai/request

Documentação OAI-PMH:
    https://www.openarchives.org/OAI/openarchivesprotocol.html

ATENÇÃO: OAI-PMH é orientado a HARVESTING (coleta total ou por intervalo
de data / set). Este script faz coleta filtrada e busca local nos
metadados retornados — não é busca textual indexada.

Uso:
    # Listar instituições (sets) do repositório padrão
    python busca_bdtd.py --sets

    # Buscar nos últimos 30 dias por palavra-chave (UFRGS por padrão)
    python busca_bdtd.py "ensino híbrido"

    # Apontar para outro repositório
    python busca_bdtd.py "letramento" --endpoint https://teses.usp.br/oai/request

    # Limitar resultados e formato ABNT
    python busca_bdtd.py "saúde mental" --max 20 --abnt

    # Listar endpoints conhecidos
    python busca_bdtd.py --endpoints

Limitações:
    - OAI-PMH retorna em lotes (cursor "resumptionToken")
    - Sem busca textual nativa: match local em título/resumo
    - Datas no formato YYYY-MM-DD
"""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Iterator, List, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_ENDPOINT = "https://lume.ufrgs.br/oai/request"

ENDPOINTS_CONHECIDOS = {
    "ufrgs":  "https://lume.ufrgs.br/oai/request",
    "usp":    "https://teses.usp.br/oai/request",
    "ufmg":   "https://repositorio.ufmg.br/oai/request",
    "bdtd":   "https://bdtd.ibict.br/vufind/OAI/Server",  # 404 em abr/2026 — listado por completude
}

USER_AGENT = "pesquisador-br-skill/0.1 (https://github.com/DevAlissu/pesquisador-br-skill)"
TIMEOUT = 30  # segundos

# OAI_ENDPOINT é resolvido na CLI; mantido como variável de módulo para compatibilidade interna
OAI_ENDPOINT = DEFAULT_ENDPOINT

# Namespaces OAI-PMH e Dublin Core
NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
}


def _request(params: dict) -> ET.Element:
    """Faz requisição GET ao endpoint OAI-PMH e devolve raiz XML."""
    url = f"{OAI_ENDPOINT}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
    try:
        return ET.fromstring(body)
    except ET.ParseError as exc:
        raise RuntimeError(f"resposta XML inválida: {exc}") from exc


def listar_sets() -> List[dict]:
    """
    Lista os 'sets' (instituições) disponíveis na BDTD.
    Cada set tem 'spec' (identificador) e 'name' (descrição).
    """
    root = _request({"verb": "ListSets"})
    sets = []
    for s in root.findall(".//oai:set", NS):
        spec = s.findtext("oai:setSpec", default="", namespaces=NS)
        name = s.findtext("oai:setName", default="", namespaces=NS)
        sets.append({"spec": spec, "name": name})
    return sets


def buscar_registros(
    set_spec: Optional[str] = None,
    desde: Optional[str] = None,
    ate: Optional[str] = None,
    metadata_prefix: str = "oai_dc",
    max_lotes: int = 5,
) -> Iterator[dict]:
    """
    Coleta registros via ListRecords. Yield de dicts com metadados Dublin Core.

    Parâmetros:
        set_spec: filtro por instituição (ex: 'com_ufrgs')
        desde: data inicial YYYY-MM-DD (filtra "from")
        ate: data final YYYY-MM-DD (filtra "until")
        metadata_prefix: oai_dc (padrão), pode haver outros
        max_lotes: limita iterações de resumptionToken (proteção contra loop)
    """
    params = {"verb": "ListRecords", "metadataPrefix": metadata_prefix}
    if set_spec:
        params["set"] = set_spec
    if desde:
        params["from"] = desde
    if ate:
        params["until"] = ate

    lotes = 0
    while True:
        root = _request(params)
        for record in root.findall(".//oai:record", NS):
            header = record.find("oai:header", NS)
            if header is None:
                continue
            if header.get("status") == "deleted":
                continue
            yield _record_para_dict(record)

        token_el = root.find(".//oai:resumptionToken", NS)
        if token_el is None or token_el.text is None or not token_el.text.strip():
            break

        lotes += 1
        if lotes >= max_lotes:
            print(f"  (limite de {max_lotes} lotes atingido — use --max-lotes para aumentar)", file=sys.stderr)
            break

        params = {"verb": "ListRecords", "resumptionToken": token_el.text}


def _record_para_dict(record: ET.Element) -> dict:
    """Converte um record OAI-PMH em dict serializável."""
    header = record.find("oai:header", NS)
    metadata = record.find(".//oai_dc:dc", NS)

    identificador = header.findtext("oai:identifier", default="", namespaces=NS) if header is not None else ""
    timestamp = header.findtext("oai:datestamp", default="", namespaces=NS) if header is not None else ""

    out = {
        "id": identificador,
        "timestamp": timestamp,
        "titles": [],
        "creators": [],
        "subjects": [],
        "descriptions": [],
        "publishers": [],
        "dates": [],
        "types": [],
        "languages": [],
        "identifiers": [],
        "rights": [],
    }

    if metadata is None:
        return out

    mapeamento = {
        "title": "titles",
        "creator": "creators",
        "subject": "subjects",
        "description": "descriptions",
        "publisher": "publishers",
        "date": "dates",
        "type": "types",
        "language": "languages",
        "identifier": "identifiers",
        "rights": "rights",
    }
    for tag, alvo in mapeamento.items():
        for el in metadata.findall(f"dc:{tag}", NS):
            if el.text:
                out[alvo].append(el.text.strip())

    return out


# ---------- Filtragem por palavra-chave ----------


def casa_termo(reg: dict, termos: List[str]) -> bool:
    """
    Match case-insensitive: todos os termos devem aparecer em título OU resumo.
    """
    if not termos:
        return True
    blob = " ".join(reg.get("titles", []) + reg.get("descriptions", []) + reg.get("subjects", []))
    blob_lower = blob.lower()
    return all(t.lower() in blob_lower for t in termos)


# ---------- Formatação ----------


def formatar_abnt(reg: dict) -> str:
    """Formata o registro como referência ABNT 6023."""
    autores_lista = reg.get("creators", []) or ["AUTOR DESCONHECIDO"]
    if len(autores_lista) == 1:
        autores = formatar_autor_abnt(autores_lista[0])
    elif len(autores_lista) <= 3:
        autores = "; ".join(formatar_autor_abnt(a) for a in autores_lista)
    else:
        autores = formatar_autor_abnt(autores_lista[0]) + " *et al.*"

    titulo = reg.get("titles", [""])[0] or "[sem título]"
    ano = _extrair_ano(reg.get("dates", []))
    tipo = _detectar_tipo(reg.get("types", []), reg.get("descriptions", []))
    inst = reg.get("publishers", [""])[0] if reg.get("publishers") else ""

    url = ""
    for ident in reg.get("identifiers", []):
        if ident.startswith("http"):
            url = ident
            break

    hoje = datetime.now().strftime("%d %b %Y").lower().replace(".", "")

    ref = f"{autores}. **{titulo}**. {ano}. {tipo}"
    if inst:
        ref += f" -- {inst}"
    if ano:
        ref += f", {ano}"
    if url:
        ref += f". Disponível em: {url}. Acesso em: {hoje}."
    else:
        ref += "."
    return ref


def formatar_autor_abnt(nome: str) -> str:
    """
    Tenta formatar 'Sobrenome, Nome' a partir de 'Nome Sobrenome' ou já formatado.
    Heurística simples — pode falhar com nomes compostos.
    """
    if "," in nome:
        return nome.upper().split(",", 1)[0] + "," + nome.split(",", 1)[1]
    partes = nome.strip().split()
    if len(partes) < 2:
        return nome.upper()
    sobrenome = partes[-1].upper()
    nomes = " ".join(partes[:-1])
    return f"{sobrenome}, {nomes}"


def _extrair_ano(datas: List[str]) -> str:
    """Pega o primeiro YYYY que encontrar."""
    for d in datas:
        m = re.search(r"(1[89]\d{2}|20\d{2})", d)
        if m:
            return m.group(1)
    return ""


def _detectar_tipo(tipos: List[str], descricoes: List[str]) -> str:
    """Decide entre Tese / Dissertação / Trabalho com base no metadado dc:type."""
    blob = " ".join(tipos + descricoes).lower()
    if "doctoral" in blob or "doutorado" in blob or "tese" in blob:
        return "Tese (Doutorado)"
    if "master" in blob or "mestrado" in blob or "dissertação" in blob:
        return "Dissertação (Mestrado)"
    return "Trabalho acadêmico"


def formatar_resumo(reg: dict, idx: int) -> str:
    titulo = reg.get("titles", [""])[0] or "[sem título]"
    autor = reg.get("creators", [""])[0] if reg.get("creators") else "[autor desconhecido]"
    ano = _extrair_ano(reg.get("dates", [])) or "?"
    tipo = _detectar_tipo(reg.get("types", []), reg.get("descriptions", []))
    return f"#{idx} [{ano}] {tipo}\n   {titulo}\n   por {autor}"


# ---------- CLI ----------


def main() -> int:
    global OAI_ENDPOINT

    parser = argparse.ArgumentParser(
        description="Coleta de teses/dissertações via OAI-PMH (UFRGS Lume por padrão; também funciona com USP, UFMG, etc)."
    )
    parser.add_argument("termos", nargs="*", help="Termos a buscar (todos devem casar)")
    parser.add_argument("--sets", action="store_true", help="Lista instituições (sets) do endpoint e sai")
    parser.add_argument("--endpoints", action="store_true", help="Lista endpoints conhecidos e sai")
    parser.add_argument(
        "--endpoint",
        default=DEFAULT_ENDPOINT,
        help=f"URL OAI-PMH (padrão: {DEFAULT_ENDPOINT}). Aceita também alias: ufrgs, usp, ufmg, bdtd",
    )
    parser.add_argument("--set", dest="set_spec", help="Filtra por set/coleção (depende do endpoint)")
    parser.add_argument("--desde", help="Data inicial (YYYY-MM-DD). Padrão: 30 dias atrás")
    parser.add_argument("--ate", help="Data final (YYYY-MM-DD)")
    parser.add_argument("--max", type=int, default=20, help="Máximo de resultados (padrão: 20)")
    parser.add_argument("--max-lotes", type=int, default=5, help="Limite de lotes OAI-PMH (padrão: 5 = ~500 registros)")
    parser.add_argument("--abnt", action="store_true", help="Imprime no formato ABNT 6023")
    args = parser.parse_args()

    if args.endpoints:
        print("=== Endpoints OAI-PMH conhecidos ===\n")
        for alias, url in ENDPOINTS_CONHECIDOS.items():
            print(f"  {alias:8s} {url}")
        print("\nUso: --endpoint <alias> ou --endpoint <url completa>")
        return 0

    # Resolve alias para URL
    if args.endpoint in ENDPOINTS_CONHECIDOS:
        OAI_ENDPOINT = ENDPOINTS_CONHECIDOS[args.endpoint]
    else:
        OAI_ENDPOINT = args.endpoint

    if args.sets:
        try:
            sets = listar_sets()
        except Exception as exc:
            print(f"❌ Erro ao consultar {OAI_ENDPOINT}: {exc}", file=sys.stderr)
            return 1
        print(f"=== {len(sets)} sets em {OAI_ENDPOINT} ===\n")
        for s in sets[:60]:
            print(f"  {s['spec']:35s} {s['name']}")
        if len(sets) > 60:
            print(f"\n  ... e mais {len(sets) - 60}. Use grep para filtrar.")
        return 0

    if not args.termos and not args.set_spec:
        parser.print_help()
        print("\nDica: use --sets para listar instituições, ou passe termos.", file=sys.stderr)
        return 2

    desde = args.desde or (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    print(f"Consultando {OAI_ENDPOINT} (set={args.set_spec or '*'}, from={desde}, until={args.ate or 'agora'})...", file=sys.stderr)

    encontrados: List[dict] = []
    try:
        for reg in buscar_registros(
            set_spec=args.set_spec,
            desde=desde,
            ate=args.ate,
            max_lotes=args.max_lotes,
        ):
            if casa_termo(reg, args.termos):
                encontrados.append(reg)
                if len(encontrados) >= args.max:
                    break
    except Exception as exc:
        print(f"❌ Erro ao consultar {OAI_ENDPOINT}: {exc}", file=sys.stderr)
        return 1

    if not encontrados:
        print("(nenhum resultado encontrado nos critérios)")
        return 0

    print(f"\n=== {len(encontrados)} resultado(s) ===\n")
    for i, reg in enumerate(encontrados, 1):
        if args.abnt:
            print(formatar_abnt(reg))
            print()
        else:
            print(formatar_resumo(reg, i))
            print()

    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
