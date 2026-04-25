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
import ipaddress
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Iterator, List, Optional
from urllib.parse import urlencode, urlparse
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

# Namespaces OAI-PMH e Dublin Core
NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
}

# Hosts/redes que NUNCA devem ser usadas como endpoint OAI-PMH (SSRF protection)
HOSTS_BLOQUEADOS = frozenset({
    "localhost", "ip6-localhost", "ip6-loopback",
})


def validar_endpoint(url: str) -> str:
    """
    Valida URL de endpoint OAI-PMH para evitar SSRF.

    Bloqueia:
      - esquemas que não sejam http/https (file://, ftp://, gopher://, etc)
      - hosts loopback (localhost, 127.0.0.0/8, ::1)
      - link-local / metadata cloud (169.254.0.0/16)
      - redes privadas (10/8, 172.16/12, 192.168/16, fc00::/7)
      - URL sem host

    Retorna a URL validada.
    Levanta ValueError em caso de bloqueio.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"esquema {parsed.scheme!r} não permitido (use http ou https)")
    if not parsed.hostname:
        raise ValueError(f"URL sem host: {url!r}")

    host = parsed.hostname.lower()
    if host in HOSTS_BLOQUEADOS:
        raise ValueError(f"host bloqueado: {host}")

    # Bloqueia IPs literais que sejam loopback / link-local / privados
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_loopback or ip.is_link_local or ip.is_private or ip.is_multicast or ip.is_reserved:
            raise ValueError(f"endereço IP local/privado bloqueado: {host}")
    except ValueError as exc:
        # Se a string não é um IP válido, ipaddress.ip_address levanta ValueError —
        # nesse caso é hostname e seguimos sem bloquear (DNS é resolvido pelo socket).
        if "bloqueado" in str(exc):
            raise

    return url


def _request(endpoint: str, params: dict) -> ET.Element:
    """Faz requisição GET ao endpoint OAI-PMH e devolve raiz XML."""
    validar_endpoint(endpoint)
    url = f"{endpoint}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
    try:
        return ET.fromstring(body)
    except ET.ParseError as exc:
        raise RuntimeError(f"resposta XML inválida: {exc}") from exc


def listar_sets(endpoint: str) -> List[dict]:
    """
    Lista os 'sets' (instituições) disponíveis no endpoint OAI-PMH.
    Cada set tem 'spec' (identificador) e 'name' (descrição).
    """
    root = _request(endpoint, {"verb": "ListSets"})
    sets = []
    for s in root.findall(".//oai:set", NS):
        spec = s.findtext("oai:setSpec", default="", namespaces=NS)
        name = s.findtext("oai:setName", default="", namespaces=NS)
        sets.append({"spec": spec, "name": name})
    return sets


def buscar_registros(
    endpoint: str,
    set_spec: Optional[str] = None,
    desde: Optional[str] = None,
    ate: Optional[str] = None,
    metadata_prefix: str = "oai_dc",
    max_lotes: int = 5,
) -> Iterator[dict]:
    """
    Coleta registros via ListRecords. Yield de dicts com metadados Dublin Core.

    Parâmetros:
        endpoint: URL OAI-PMH (validada por validar_endpoint)
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
        root = _request(endpoint, params)
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


# ---------- Auto-teste ----------


def auto_teste() -> int:
    """
    Testes embutidos das funções puras (validar_endpoint, _extrair_ano,
    formatar_autor_abnt). Não faz chamadas HTTP. Retorna 0 se todos passarem.
    """
    erros = 0

    # validar_endpoint — casos OK
    for url in [
        "https://lume.ufrgs.br/oai/request",
        "http://exemplo.org/oai",
        "https://teses.usp.br/oai/request?ignored=1",
    ]:
        try:
            validar_endpoint(url)
            print(f"  [OK]   validar_endpoint accept {url!r}")
        except Exception as exc:
            print(f"  [FAIL] validar_endpoint deveria aceitar {url!r}: {exc}")
            erros += 1

    # validar_endpoint — casos REJEITAR
    for url in [
        "file:///etc/passwd",
        "ftp://evil.example.com/",
        "gopher://x/",
        "http://localhost:8080/",
        "http://127.0.0.1/",
        "http://169.254.169.254/latest/meta-data/",  # AWS/GCP metadata
        "http://10.0.0.5/",
        "http://192.168.1.1/",
        "http://[::1]/",
        "https://",  # sem host
    ]:
        try:
            validar_endpoint(url)
            print(f"  [FAIL] validar_endpoint deveria REJEITAR {url!r}")
            erros += 1
        except ValueError:
            print(f"  [OK]   validar_endpoint reject {url!r}")

    # _extrair_ano
    casos_ano = [
        (["2020-04-15"], "2020"),
        (["2024-01-01T00:00:00Z"], "2024"),
        (["sem ano"], ""),
        ([], ""),
        (["1999-12-31", "2030-01-01"], "1999"),  # primeiro ganha
    ]
    for entrada, esperado in casos_ano:
        obtido = _extrair_ano(entrada)
        if obtido == esperado:
            print(f"  [OK]   _extrair_ano({entrada!r}) -> {obtido!r}")
        else:
            print(f"  [FAIL] _extrair_ano({entrada!r}) = {obtido!r}, esperava {esperado!r}")
            erros += 1

    # formatar_autor_abnt
    casos_autor = [
        ("José Alberto Silva", "SILVA, José Alberto"),
        ("Silva, José", "SILVA, José"),     # já formatado
        ("Maria", "MARIA"),                 # nome único
        ("M. C. S. Minayo", "MINAYO, M. C. S."),
    ]
    for entrada, esperado in casos_autor:
        obtido = formatar_autor_abnt(entrada)
        if obtido == esperado:
            print(f"  [OK]   formatar_autor_abnt({entrada!r}) -> {obtido!r}")
        else:
            print(f"  [FAIL] formatar_autor_abnt({entrada!r}) = {obtido!r}, esperava {esperado!r}")
            erros += 1

    if erros:
        print(f"\n❌ {erros} caso(s) falharam")
        return 1
    print("\n✅ Todos os testes passaram")
    return 0


# ---------- CLI ----------


def main() -> int:
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
    parser.add_argument("--teste", action="store_true", help="Roda auto-teste (sem rede) e sai")
    args = parser.parse_args()

    if args.teste:
        return auto_teste()

    if args.endpoints:
        print("=== Endpoints OAI-PMH conhecidos ===\n")
        for alias, url in ENDPOINTS_CONHECIDOS.items():
            print(f"  {alias:8s} {url}")
        print("\nUso: --endpoint <alias> ou --endpoint <url completa>")
        return 0

    # Resolve alias para URL e valida (anti-SSRF)
    endpoint = ENDPOINTS_CONHECIDOS.get(args.endpoint, args.endpoint)
    try:
        endpoint = validar_endpoint(endpoint)
    except ValueError as exc:
        print(f"❌ Endpoint rejeitado: {exc}", file=sys.stderr)
        print("   Use --endpoints para ver opções confiáveis.", file=sys.stderr)
        return 2

    if args.sets:
        try:
            sets = listar_sets(endpoint)
        except Exception as exc:
            print(f"❌ Erro ao consultar {endpoint}: {exc}", file=sys.stderr)
            return 1
        print(f"=== {len(sets)} sets em {endpoint} ===\n")
        for s in sets[:60]:
            print(f"  {s['spec']:35s} {s['name']}")
        if len(sets) > 60:
            print(f"\n  ... e mais {len(sets) - 60}. Use grep para filtrar.")
        return 0

    if not args.termos and not args.set_spec:
        parser.print_help()
        print("\nDica: use --sets para listar instituições, --endpoints para listar repositórios, ou passe termos.", file=sys.stderr)
        return 2

    desde = args.desde or (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    print(f"Consultando {endpoint} (set={args.set_spec or '*'}, from={desde}, until={args.ate or 'agora'})...", file=sys.stderr)

    encontrados: List[dict] = []
    try:
        for reg in buscar_registros(
            endpoint,
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
        print(f"❌ Erro ao consultar {endpoint}: {exc}", file=sys.stderr)
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
