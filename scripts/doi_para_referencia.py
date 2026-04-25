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

    req = Request(url, headers={'User-Agent': 'pesquisador-br-skill/0.1 (mailto:contato@example.com)'})
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


def main():
    parser = argparse.ArgumentParser(
        description='Converte DOI em referência ABNT 6023 usando CrossRef.',
    )
    parser.add_argument('doi', help='DOI (com ou sem prefixo URL)')
    parser.add_argument('--json-out', action='store_true', help='Output JSON com metadata')

    args = parser.parse_args()

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
    main()
