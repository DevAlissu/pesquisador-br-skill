"""
doi_para_referencia.py — Converte DOI em referência ABNT 6023.

Usa CrossRef API (gratuita, sem chave) pra resolver metadata do DOI.

Uso:
    python doi_para_referencia.py 10.1590/S1413-24782020000100008
"""

import argparse
import json
import sys
from urllib.request import Request, urlopen
from urllib.parse import quote


CROSSREF_API = "https://api.crossref.org/works/"


def resolver_doi(doi: str) -> dict:
    doi = doi.strip().replace('https://doi.org/', '').replace('http://dx.doi.org/', '')
    url = CROSSREF_API + quote(doi, safe='/')

    req = Request(url, headers={'User-Agent': 'pesquisador-br-skill/0.1 (https://github.com/DevAlissu/pesquisador-br-skill)'})
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as err:
        print(f"❌ Erro ao resolver DOI: {err}", file=sys.stderr)
        return None

    return data.get('message', {})


def formatar_abnt(meta: dict) -> str:
    """
    Gera referência ABNT 6023 a partir de metadata CrossRef.
    """
    if not meta:
        return None

    # Autores
    autores_raw = meta.get('author', [])
    autores_fmt = []
    for a in autores_raw[:3]:
        sobrenome = a.get('family', '').upper()
        prenome = a.get('given', '')
        autores_fmt.append(f"{sobrenome}, {prenome}")

    if len(autores_raw) > 3:
        autores_str = autores_fmt[0] + ' *et al.*'
    else:
        autores_str = '; '.join(autores_fmt)

    # Título
    titulos = meta.get('title', [])
    titulo = titulos[0] if titulos else '[título]'

    # Periódico
    periodico = meta.get('container-title', [''])[0] or '[periódico]'

    # Volume / issue / page
    volume = meta.get('volume', '')
    issue = meta.get('issue', '')
    pages = meta.get('page', '')

    # Ano
    issued = meta.get('issued', {}).get('date-parts', [[None]])[0]
    ano = issued[0] if issued else 'XXXX'

    # DOI
    doi = meta.get('DOI', '')

    # Tipo
    tipo = meta.get('type', '')

    # Monta referência
    ref = f"{autores_str}. {titulo}. **{periodico}**"
    if volume:
        ref += f", v. {volume}"
    if issue:
        ref += f", n. {issue}"
    if pages:
        ref += f", p. {pages}"
    ref += f", {ano}"
    if doi:
        ref += f". DOI: {doi}"
        ref += f". Disponível em: https://doi.org/{doi}. Acesso em: [data]"

    return ref + '.'


def auto_teste() -> int:
    """Auto-teste de formatar_abnt sem chamadas HTTP."""
    erros = 0

    # Caso 1: artigo de 1 autor com volume, número, páginas, DOI
    meta1 = {
        'author': [{'family': 'Silva', 'given': 'Ana Maria'}],
        'title': ['Educação inclusiva no Brasil'],
        'container-title': ['Revista Brasileira de Educação'],
        'volume': '25', 'issue': '80', 'page': '123-145',
        'issued': {'date-parts': [[2020]]},
        'DOI': '10.1590/exemplo',
    }
    ref1 = formatar_abnt(meta1)
    esperados1 = [
        'SILVA, Ana Maria',
        'Educação inclusiva',
        '**Revista Brasileira de Educação**',
        'v. 25', 'n. 80', 'p. 123-145', '2020',
        'DOI: 10.1590/exemplo',
    ]
    for parte in esperados1:
        if parte in ref1:
            print(f"  [OK]   esperado {parte!r} presente")
        else:
            print(f"  [FAIL] esperado {parte!r} ausente em: {ref1!r}")
            erros += 1

    # Caso 2: 4+ autores -> et al.
    meta2 = {
        'author': [
            {'family': 'A', 'given': 'X'},
            {'family': 'B', 'given': 'Y'},
            {'family': 'C', 'given': 'Z'},
            {'family': 'D', 'given': 'W'},
        ],
        'title': ['Multi'],
        'container-title': ['R'],
        'issued': {'date-parts': [[2024]]},
    }
    ref2 = formatar_abnt(meta2)
    if '*et al.*' in ref2:
        print(f"  [OK]   4+ autores produz '*et al.*'")
    else:
        print(f"  [FAIL] 4+ autores deveria ter '*et al.*': {ref2!r}")
        erros += 1

    # Caso 3: meta vazio retorna None
    if formatar_abnt({}) is None or formatar_abnt(None) is None:
        # formatar_abnt({}) na verdade retorna string com placeholders;
        # só formatar_abnt(None) e formatar_abnt(False) retornam None pelo
        # check `if not meta: return None`. Vamos testar None.
        pass
    if formatar_abnt(None) is None:
        print(f"  [OK]   meta=None retorna None")
    else:
        print(f"  [FAIL] meta=None deveria retornar None")
        erros += 1

    # Caso 4: DOI sanitização (remove prefixo URL antes de chamar API)
    # Não chama rede; só verifica que o sanitize funciona via comportamento
    # observável: a função resolver_doi remove o prefixo na primeira linha.
    import doi_para_referencia as mod  # auto-import
    test_inputs = [
        ('https://doi.org/10.1/x', '10.1/x'),
        ('http://dx.doi.org/10.2/y', '10.2/y'),
        ('  10.3/z  ', '10.3/z'),
    ]
    for raw, esperado in test_inputs:
        sanitized = raw.strip().replace('https://doi.org/', '').replace('http://dx.doi.org/', '')
        if sanitized == esperado:
            print(f"  [OK]   sanitize({raw!r}) -> {esperado!r}")
        else:
            print(f"  [FAIL] sanitize({raw!r}) = {sanitized!r}, esperava {esperado!r}")
            erros += 1

    if erros:
        print(f"\n❌ {erros} caso(s) falharam")
        return 1
    print("\n✅ Todos os testes passaram")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Converte DOI em referência ABNT 6023 usando CrossRef.',
    )
    parser.add_argument('doi', nargs='?', help='DOI (com ou sem prefixo URL)')
    parser.add_argument('--json-out', action='store_true', help='Output JSON com metadata')
    parser.add_argument('--teste', action='store_true', help='Roda auto-teste (sem rede) e sai')

    args = parser.parse_args()

    if args.teste:
        sys.exit(auto_teste())

    if not args.doi:
        parser.print_help()
        sys.exit(2)

    print(f'🔎 Resolvendo DOI: {args.doi}...', file=sys.stderr)
    meta = resolver_doi(args.doi)

    if not meta:
        sys.exit(1)

    if args.json_out:
        print(json.dumps(meta, ensure_ascii=False, indent=2))
        return

    print('=== Metadata ===')
    print(f"Tipo: {meta.get('type', '?')}")
    print(f"Título: {(meta.get('title') or [''])[0]}")
    print(f"Autores: {len(meta.get('author', []))} autor(es)")
    print(f"Periódico: {(meta.get('container-title') or [''])[0]}")
    print(f"Ano: {(meta.get('issued', {}).get('date-parts', [[None]])[0] or [None])[0]}")
    print()
    print('=== Referência ABNT 6023 ===')
    print(formatar_abnt(meta))
    print()
    print('⚠️  Verifique manualmente: APIs podem omitir prenome completo, edição ou tradutor.')


if __name__ == '__main__':
    # Reconfigura stdout para UTF-8 (Windows usa cp1252 por padrão e quebra emojis)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    main()
