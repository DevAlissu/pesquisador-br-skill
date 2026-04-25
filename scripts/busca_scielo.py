"""
busca_scielo.py — Busca programática no SciELO Brasil.

Uso:
    python busca_scielo.py "ensino híbrido" --ano 2020-2026 --max 30

Retorna lista de artigos com título, autores, periódico, ano, DOI, URL.
"""

import argparse
import json
import sys
from urllib.parse import quote_plus
import urllib.request


SCIELO_API = "https://search.scielo.org/api/json"


def buscar_scielo(query: str, ano_inicio: int = None, ano_fim: int = None, max_resultados: int = 30):
    """
    Busca artigos no SciELO. Retorna lista de dicts.
    """
    params = {
        'q': query,
        'lang': 'pt',
        'count': max_resultados,
        'output': 'site',
    }

    if ano_inicio and ano_fim:
        params['filter[year_cluster][]'] = f'{ano_inicio}-{ano_fim}'

    url = f"{SCIELO_API}?" + "&".join([f"{k}={quote_plus(str(v))}" for k, v in params.items()])

    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read())
    except Exception as err:
        print(f"❌ Erro na busca SciELO: {err}", file=sys.stderr)
        return []

    resultados = []
    for doc in data.get('diaServerResponse', [{}])[0].get('response', {}).get('docs', []):
        resultados.append({
            'titulo': doc.get('ti', ''),
            'autores': doc.get('au', []),
            'periodico': doc.get('journal_title', ''),
            'ano': doc.get('da', '')[:4] if doc.get('da') else '',
            'volume': doc.get('volume', ''),
            'issue': doc.get('issue', ''),
            'idioma': doc.get('la', ''),
            'doi': doc.get('doi', ''),
            'url': doc.get('url', ''),
            'resumo': doc.get('ab', '')[:300] + '...' if doc.get('ab') else '',
        })

    return resultados


def formatar_referencia_abnt(art: dict) -> str:
    """
    Tenta gerar referência ABNT 6023 baseada nos dados do SciELO.
    Sempre verifique manualmente — APIs nem sempre trazem todos os campos.
    """
    autores = art.get('autores', [])
    autores_fmt = []
    for a in autores[:3]:
        partes = a.split(',', 1)
        sobrenome = partes[0].strip().upper()
        prenome = partes[1].strip() if len(partes) > 1 else ''
        autores_fmt.append(f"{sobrenome}, {prenome}")

    if len(autores) > 3:
        autores_str = autores_fmt[0] + ' *et al.*'
    else:
        autores_str = '; '.join(autores_fmt)

    titulo = art.get('titulo', '[título]')
    periodico = art.get('periodico', '[periódico]')
    ano = art.get('ano', 'XXXX')
    volume = art.get('volume', '')
    issue = art.get('issue', '')
    doi = art.get('doi', '')
    url = art.get('url', '')

    ref = f"{autores_str}. {titulo}. **{periodico}**"
    if volume:
        ref += f", v. {volume}"
    if issue:
        ref += f", n. {issue}"
    ref += f", {ano}"
    if doi:
        ref += f". DOI: {doi}"
    if url:
        ref += f". Disponível em: {url}. Acesso em: [data]"

    return ref + '.'


def main():
    parser = argparse.ArgumentParser(
        description='Busca artigos no SciELO Brasil e gera referências ABNT.',
    )
    parser.add_argument('query', help='Termo de busca (entre aspas se tiver espaços)')
    parser.add_argument('--ano-inicio', type=int, help='Ano inicial')
    parser.add_argument('--ano-fim', type=int, help='Ano final')
    parser.add_argument('--max', type=int, default=30, help='Máx resultados (default: 30)')
    parser.add_argument('--abnt', action='store_true', help='Gera referências ABNT')
    parser.add_argument('--json-out', action='store_true', help='Output em JSON')

    args = parser.parse_args()

    print(f'🔎 Buscando "{args.query}" no SciELO Brasil...', file=sys.stderr)
    resultados = buscar_scielo(
        args.query,
        ano_inicio=args.ano_inicio,
        ano_fim=args.ano_fim,
        max_resultados=args.max,
    )

    print(f'✅ {len(resultados)} resultados encontrados.\n', file=sys.stderr)

    if args.json_out:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
        return

    for i, art in enumerate(resultados, 1):
        print(f'--- {i} ---')
        print(f"Título: {art['titulo']}")
        print(f"Autores: {', '.join(art['autores'])}")
        print(f"Periódico: {art['periodico']} ({art['ano']})")
        if art['doi']:
            print(f"DOI: {art['doi']}")
        if args.abnt:
            print(f"\nReferência ABNT:\n{formatar_referencia_abnt(art)}")
        print()


if __name__ == '__main__':
    main()
