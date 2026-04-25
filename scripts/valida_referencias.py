"""
valida_referencias.py — Validação heurística de referências no formato ABNT NBR 6023:2018.

Este script aplica regras regex para detectar problemas FREQUENTES em listas de
referências bibliográficas em PT-BR. Não substitui a revisão humana — sinaliza
candidatos a inspeção. Cobre:

- Sobrenome em MAIÚSCULAS
- Presença de ano
- Uso correto de "et al." (3+ autores)
- Indicação de tipo de fonte (livro, artigo, tese, online)
- Acesso (Disponível em / Acesso em) para fontes online
- Páginas para artigos
- Cidade + editora para livros

Uso:
    python valida_referencias.py referencias.txt
    python valida_referencias.py referencias.txt --strict
    cat referencias.txt | python valida_referencias.py -
    python valida_referencias.py --teste

Saída:
    - Lista de avisos por referência
    - Código de saída 0 (todas OK) ou 1 (alguma com aviso)

Limitações:
    - Heurística: pode dar falso positivo / negativo
    - Não verifica DOI / ISSN / ISBN reais (use doi_para_referencia.py para isso)
    - Não checa formato exato de edição, volume, número
"""

import argparse
import re
import sys
from typing import List, Tuple


# ---------- Regras (regex) ----------

REGEX_SOBRENOME_MAIUSCULAS = re.compile(r"^([A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}(?:[\s\-][A-ZÁÉÍÓÚÂÊÔÃÕÇ]+)*),\s")
REGEX_ANO = re.compile(r"\b(1[89]\d{2}|20\d{2})\b")
REGEX_ET_AL = re.compile(r"\bet\s+al\.?\b", re.IGNORECASE)
REGEX_DISPONIVEL_EM = re.compile(r"\bDispon[íi]vel\s+em:\s*<?https?://", re.IGNORECASE)
REGEX_ACESSO_EM = re.compile(r"\bAcesso\s+em:\s*\d", re.IGNORECASE)
REGEX_PAGINAS = re.compile(r"\bp\.\s*\d+(\s*[-–]\s*\d+)?", re.IGNORECASE)
REGEX_VOLUME = re.compile(r"\bv\.\s*\d+", re.IGNORECASE)
REGEX_NUMERO = re.compile(r"\bn\.\s*\d+", re.IGNORECASE)
REGEX_EDICAO = re.compile(r"\b\d+\.\s*ed\.", re.IGNORECASE)
REGEX_TESE_DISSERT = re.compile(r"\b(Tese|Disserta[çc][ãa]o|TCC|Monografia)\b", re.IGNORECASE)
REGEX_DOI = re.compile(r"\b(10\.\d{4,9}/\S+)\b")
REGEX_TITULO_ITALICO_NEGRITO = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|_[^_]+_)")

# Padrão "Cidade: Editora" — uma palavra capitalizada (ou várias),
# seguida de ":", seguida de palavra capitalizada (a editora).
# Ex: "São Paulo: Atlas", "Rio de Janeiro: ABNT", "Porto Alegre: Artmed".
REGEX_CIDADE_EDITORA = re.compile(
    r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ]+(?:\s[A-ZÁÉÍÓÚÂÊÔÃÕÇ\wÀ-ÿ]+)*\s*:\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ]+"
)

# Prefixos comuns em referências que NÃO são "Cidade: Editora" mas geram
# falso positivo no regex acima ("Disponível em: ABNT", "Acesso em: 24",
# "DOI: 10.1590", "ISSN: 1234-5678", "ISBN: 978-...").
PREFIXOS_FALSOS_LIVRO = (
    "Disponível",
    "Acesso",
    "DOI",
    "ISSN",
    "ISBN",
    "URL",
    "Endereço",
    "E-mail",
    "Lattes",
    "ORCID",
    "In",  # "In: SOBRENOME, ..." (capítulo de livro) — prefixo de citação, não local
)


def tem_cidade_editora(texto: str) -> bool:
    """
    True se o texto tem o padrão Cidade: Editora E não é um falso positivo
    (Disponível em: X, DOI: X, etc).
    """
    for match in REGEX_CIDADE_EDITORA.finditer(texto):
        # Palavras imediatamente antes do match (até 2)
        prefixo = texto[: match.start()].rstrip()
        ultimas_2 = prefixo.rsplit(maxsplit=2)[-2:] if prefixo else []
        ultimas_2 = [p.rstrip(".,;:") for p in ultimas_2]

        # Palavras DENTRO do match, antes do ":"
        antes_dois_pontos = match.group().split(":", 1)[0].strip().split()

        # Junta todas as palavras candidatas a prefixo conhecido
        candidatas = set(ultimas_2) | set(antes_dois_pontos)
        if candidatas & set(PREFIXOS_FALSOS_LIVRO):
            continue

        return True
    return False

# URLs comuns de bases acadêmicas (sinaliza fonte online)
DOMINIOS_ONLINE = (
    "scielo", "doi.org", "lattes", "bdtd", "capes",
    "periodicos", "ibict", "fiocruz", "lilacs",
    "pubmed", "scopus", "wiley", "elsevier", "springer",
    "github", "osf.io", "researchgate", "academia.edu",
)


def parece_url(texto: str) -> bool:
    return any(d in texto.lower() for d in DOMINIOS_ONLINE) or "http" in texto


def parece_artigo(texto: str) -> bool:
    """Heurística: tem volume, número e páginas."""
    return bool(REGEX_VOLUME.search(texto) or REGEX_NUMERO.search(texto)) and bool(REGEX_PAGINAS.search(texto))


def parece_tese(texto: str) -> bool:
    return bool(REGEX_TESE_DISSERT.search(texto))


def parece_livro(texto: str) -> bool:
    """
    Heurística: aparenta ser livro se tem indicação de edição (3. ed.) OU
    padrão Cidade: Editora visível (filtrando falsos positivos como
    "Disponível em:", "DOI:", "ISSN:"). Exclui artigos e teses primeiro.
    """
    if parece_artigo(texto) or parece_tese(texto):
        return False
    return bool(REGEX_EDICAO.search(texto)) or tem_cidade_editora(texto)


# ---------- Validações por referência ----------


def validar_referencia(ref: str, strict: bool = False) -> List[str]:
    """
    Retorna lista de avisos. Lista vazia = referência aparenta estar OK.
    """
    avisos: List[str] = []
    ref_strip = ref.strip()

    if not ref_strip:
        return ["referência vazia"]

    # 1. Sobrenome em maiúsculas
    if not REGEX_SOBRENOME_MAIUSCULAS.match(ref_strip):
        avisos.append("sobrenome do primeiro autor não está em MAIÚSCULAS seguido de vírgula")

    # 2. Ano
    if not REGEX_ANO.search(ref_strip):
        avisos.append("não foi detectado ano (1800-2099)")

    # 3. Tipo (artigo / tese / livro / online)
    eh_online = parece_url(ref_strip)
    eh_artigo = parece_artigo(ref_strip)
    eh_tese = parece_tese(ref_strip)
    eh_livro = parece_livro(ref_strip)

    # 4. Páginas em artigo
    if eh_artigo and not REGEX_PAGINAS.search(ref_strip):
        avisos.append("aparenta ser artigo, mas não tem indicação de páginas (p. XX-YY)")

    # 5. Disponível em / Acesso em (se for online)
    if eh_online:
        if not REGEX_DISPONIVEL_EM.search(ref_strip):
            avisos.append("fonte online sem 'Disponível em: <url>'")
        if not REGEX_ACESSO_EM.search(ref_strip):
            avisos.append("fonte online sem 'Acesso em: dia mês ano'")

    # 6. Tese/dissertação: deve ter "Tese/Dissertação (...) -- Universidade..."
    if eh_tese and "--" not in ref_strip and "—" not in ref_strip:
        avisos.append("tese/dissertação sem separador '--' antes da instituição")

    # 7. Livro: cidade + editora (heurística — só dispara se a edição foi indicada
    #    mas o padrão "Cidade: Editora" não é detectável, ignorando falsos positivos)
    if eh_livro and not tem_cidade_editora(ref_strip):
        avisos.append("aparenta ser livro (tem edição), mas não foi detectado padrão 'Cidade: Editora'")

    # 8. et al. — deve estar em itálico ou marcado (heurística leve)
    et_al_match = REGEX_ET_AL.search(ref_strip)
    if et_al_match and strict:
        # NBR 6023 admite "et al." em itálico ou romano. Apenas avisa em strict.
        avisos.append("'et al.' encontrado — verifique se há até 3 autores listados antes")

    # 9. Strict: avisa se faltar título destacado (negrito ou itálico em markdown)
    if strict and not REGEX_TITULO_ITALICO_NEGRITO.search(ref_strip):
        avisos.append("nenhum trecho aparece em negrito (**...**) ou itálico (*...*) — confira destaque do título")

    return avisos


# ---------- Parsing de arquivo ----------


def carregar_referencias(fonte) -> List[str]:
    """
    Lê referências de um arquivo (uma por bloco, separado por linha em branco)
    ou de um arquivo com uma referência por linha. Tenta detectar.
    """
    texto = fonte.read()
    # Estratégia: se há linhas em branco, separa por blocos (parágrafo).
    # Caso contrário, separa por quebra simples.
    if "\n\n" in texto:
        blocos = [b.strip() for b in texto.split("\n\n") if b.strip()]
    else:
        blocos = [linha.strip() for linha in texto.splitlines() if linha.strip()]
    return blocos


# ---------- Auto-teste ----------


def auto_teste() -> int:
    """
    Casos de teste embutidos. Retorna 0 se todos passarem.
    """
    casos: List[Tuple[str, bool]] = [
        # (referência, deve passar sem avisos?)

        # OK — artigo SciELO
        (
            "MINAYO, M. C. S. Análise qualitativa: teoria, passos e fidedignidade. "
            "*Ciência & Saúde Coletiva*, v. 17, n. 3, p. 621-626, mar. 2012. "
            "DOI: 10.1590/S1413-81232012000300007. "
            "Disponível em: <https://www.scielo.br/scielo.php?pid=S1413-81232012000300007>. "
            "Acesso em: 24 abr. 2026.",
            True,
        ),

        # OK — livro com Cidade: Editora bem formatado
        (
            "GIL, A. C. **Como elaborar projetos de pesquisa**. 6. ed. "
            "São Paulo: Atlas, 2017.",
            True,
        ),

        # FALHA — sem ano
        (
            "GIL, A. C. Como elaborar projetos de pesquisa. Atlas.",
            False,
        ),

        # FALHA — sobrenome em minúsculo
        (
            "gil, a. c. Como elaborar projetos de pesquisa. 6. ed. São Paulo: Atlas, 2017.",
            False,
        ),

        # FALHA — livro (tem edição) mas SEM cidade: editora
        (
            "ALBUQUERQUE, J. *Estudos críticos*. 3. ed. Atlas 2020.",
            False,
        ),
    ]

    # Testes unitários de tem_cidade_editora (falso positivo de prefixos)
    casos_cidade_editora: List[Tuple[str, bool]] = [
        ("São Paulo: Atlas, 2017", True),
        ("Rio de Janeiro: ABNT, 2018", True),
        ("Porto Alegre: Artmed, 2020", True),
        ("Disponível em: ABNT", False),         # falso positivo histórico
        ("Acesso em: 24 abr. 2026", False),     # mês não capitalizado, mas Acesso prefixo
        ("DOI: 10.1590/exemplo", False),        # "10" não é capital
        ("ISSN: 1234-5678", False),
        ("In: SILVA, J. (org.). Livro. São Paulo: Atlas, 2020", True),  # In: ignorado, mas SP:Atlas casa
    ]
    erros = 0
    for entrada, esperado in casos_cidade_editora:
        obtido = tem_cidade_editora(entrada)
        if obtido == esperado:
            print(f"  [OK]   tem_cidade_editora({entrada!r}) -> {obtido}")
        else:
            print(f"  [FAIL] tem_cidade_editora({entrada!r}) = {obtido}, esperava {esperado}")
            erros += 1

    for i, (ref, deve_passar) in enumerate(casos, 1):
        avisos = validar_referencia(ref)
        passou = len(avisos) == 0
        ok = passou == deve_passar
        marca = "OK" if ok else "FAIL"
        print(f"  [{marca}] caso {i}: deve_passar={deve_passar}, passou={passou}, avisos={len(avisos)}")
        if not ok:
            erros += 1
            for a in avisos:
                print(f"        - {a}")

    if erros:
        print(f"\n❌ {erros} caso(s) de teste falharam")
        return 1
    print("\n✅ Todos os testes passaram")
    return 0


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador heurístico de referências ABNT NBR 6023:2018."
    )
    parser.add_argument(
        "arquivo",
        nargs="?",
        help="Caminho do .txt com referências (uma por bloco). Use '-' para stdin.",
    )
    parser.add_argument("--strict", action="store_true", help="Aplica regras opcionais (et al., destaque de título).")
    parser.add_argument("--teste", action="store_true", help="Roda auto-teste e sai.")
    args = parser.parse_args()

    if args.teste:
        return auto_teste()

    if not args.arquivo:
        parser.print_help()
        return 2

    if args.arquivo == "-":
        refs = carregar_referencias(sys.stdin)
    else:
        try:
            with open(args.arquivo, encoding="utf-8") as f:
                refs = carregar_referencias(f)
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {args.arquivo}", file=sys.stderr)
            return 2

    if not refs:
        print("(nenhuma referência encontrada)")
        return 0

    total_avisos = 0
    for i, ref in enumerate(refs, 1):
        avisos = validar_referencia(ref, strict=args.strict)
        if avisos:
            total_avisos += len(avisos)
            print(f"\n--- Referência #{i} ---")
            print(f"  {ref[:120]}{'...' if len(ref) > 120 else ''}")
            for a in avisos:
                print(f"  ⚠️  {a}")

    print(f"\n=== Resumo ===")
    print(f"  Total de referências: {len(refs)}")
    print(f"  Avisos detectados:   {total_avisos}")

    return 0 if total_avisos == 0 else 1


if __name__ == "__main__":
    # Reconfigura stdout para UTF-8 (Windows usa cp1252 por padrão e quebra emojis)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
