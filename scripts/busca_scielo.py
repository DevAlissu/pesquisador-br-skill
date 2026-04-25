"""
busca_scielo.py — Busca programática no SciELO Brasil via ArticleMeta API.

API real: https://articlemeta.scielo.org/api/v1/
Documentação: https://docs.scielo.org/projects/scielo-pc-programs/en/latest/articlemeta_api.html

Uso:
    python busca_scielo.py "ensino híbrido" --max 30
    python busca_scielo.py "blended learning" --colecao bra --abnt
"""

import argparse
import json
import sys
from urllib.parse import quote_plus
from urllib.request import Request, urlopen


# Endpoints reais
ARTICLEMETA_BASE = "https://articlemeta.scielo.org/api/v1"
SCIELO_SEARCH_URL = "https://search.scielo.org/?q={query}&lang=pt&format=json&count={count}"
USER_AGENT = "pesquisador-br-skill/0.1 (https://github.com/DevAlissu/pesquisador-br-skill)"


def buscar_scielo_search(query: str, max_resultados: int = 30, lang: str = "pt"):
    """
    Busca via SciELO search frontend (retorna HTML — usado como fallback).
    Pra busca programática real, prefira ArticleMeta API quando souber o ISSN/coleção.
    """
    url = f"https://search.scielo.org/?q={quote_plus(query)}&lang={lang}&count={max_resultados}&output=site"
    req = Request(url, headers={'User-Agent': USER_AGENT})

    try:
        with urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get('Content-Type', '')
            data = resp.read().decode('utf-8', errors='replace')
    except Exception as err:
        print(f"❌ Erro na busca SciELO: {err}", file=sys.stderr)
        return []

    # SciELO search retorna HTML, não JSON puro. Parse simplificado:
    # Pra extração séria, recomenda-se usar a API ArticleMeta com identificadores conhecidos.
    print(
        f"⚠️  Busca via SciELO search retornou {content_type}. "
        f"Pra extração estruturada, prefira a API ArticleMeta consultando por ISSN/PID.",
        file=sys.stderr,
    )
    print(f"🔗 URL consultada: {url}", file=sys.stderr)
    print(f"💡 Abra essa URL no navegador para ver os resultados completos.", file=sys.stderr)
    return []


def buscar_articlemeta_por_issn(issn: str, max_resultados: int = 30):
    """
    Busca artigos publicados em um periódico específico via ArticleMeta API.
    Requer ISSN do periódico.
    """
    url = f"{ARTICLEMETA_BASE}/article/identifiers/?issn={issn}&limit={max_resultados}"
    req = Request(url, headers={'User-Agent': USER_AGENT})

    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except Exception as err:
        print(f"❌ Erro na busca ArticleMeta (ISSN {issn}): {err}", file=sys.stderr)
        return []

    # Resposta tem estrutura: {"objects": [{"code": "...", "collection": "...", ...}]}
    objects = data.get('objects', [])
    resultados = []
    for obj in objects[:max_resultados]:
        code = obj.get('code')
        collection = obj.get('collection', 'scl')
        if not code:
            continue
        # Buscar metadata completa de cada artigo
        meta = _buscar_metadata_artigo(code, collection)
        if meta:
            resultados.append(meta)
    return resultados


def _buscar_metadata_artigo(pid: str, collection: str = 'scl'):
    """
    Busca metadata completa de um artigo no SciELO via ArticleMeta API.
    """
    url = f"{ARTICLEMETA_BASE}/article/?code={pid}&collection={collection}&format=xylose"
    req = Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception:
        return None

    # Estrutura "xylose" tem: title, authors, journal_title, publication_date, doi, abstract...
    return {
        'titulo': data.get('original_title') or data.get('translated_titles', {}).get('en', ''),
        'autores': [
            f"{a.get('surname', '')}, {a.get('given_names', '')}"
            for a in data.get('authors', [])
        ],
        'periodico': data.get('journal_title', ''),
        'ano': str(data.get('publication_date', ''))[:4],
        'volume': data.get('volume', ''),
        'numero': data.get('issue', ''),
        'paginas': f"{data.get('start_page', '')}-{data.get('end_page', '')}".strip('-'),
        'doi': data.get('doi', ''),
        'pid': pid,
        'colecao': collection,
        'idioma': data.get('original_language', ''),
    }


def formatar_referencia_abnt(art: dict) -> str:
    """
    Gera referência ABNT 6023:2018 a partir de metadata SciELO.
    ⚠️  APIs nem sempre trazem todos os campos — verifique manualmente.
    """
    autores = [a.strip() for a in art.get('autores', []) if a.strip(', ')]
    autores_fmt = []
    for a in autores[:3]:
        partes = [p.strip() for p in a.split(',', 1)]
        sobrenome = partes[0].upper() if partes else ''
        prenome = partes[1] if len(partes) > 1 else ''
        if sobrenome:
            autores_fmt.append(f"{sobrenome}, {prenome}".strip(', '))

    if len(autores) > 3 and autores_fmt:
        autores_str = autores_fmt[0] + ' *et al.*'
    elif autores_fmt:
        autores_str = '; '.join(autores_fmt)
    else:
        autores_str = '[autor não identificado]'

    titulo = art.get('titulo') or '[título não identificado]'
    periodico = art.get('periodico') or '[periódico não identificado]'
    ano = art.get('ano') or 'XXXX'
    volume = art.get('volume', '')
    numero = art.get('numero', '')
    paginas = art.get('paginas', '')
    doi = art.get('doi', '')

    ref = f"{autores_str}. {titulo}. **{periodico}**"
    if volume:
        ref += f", v. {volume}"
    if numero:
        ref += f", n. {numero}"
    if paginas and paginas != '-':
        ref += f", p. {paginas}"
    ref += f", {ano}"
    if doi:
        ref += f". DOI: {doi}"
        ref += f". Disponível em: https://doi.org/{doi}. Acesso em: [data]"

    return ref + '.'


def main():
    parser = argparse.ArgumentParser(
        description='Busca artigos no SciELO Brasil (via ArticleMeta API ou search frontend).',
    )
    parser.add_argument('query', nargs='?', help='Termo de busca (texto livre)')
    parser.add_argument('--issn', help='ISSN do periódico (formato XXXX-XXXX) para busca via ArticleMeta')
    parser.add_argument('--max', type=int, default=30, help='Máx resultados (default: 30)')
    parser.add_argument('--abnt', action='store_true', help='Gera referências ABNT 6023:2018')
    parser.add_argument('--json-out', action='store_true', help='Output em JSON')

    args = parser.parse_args()

    if not args.query and not args.issn:
        parser.error('Informe um termo de busca ou --issn de um periódico')

    if args.issn:
        print(f'🔎 Buscando artigos do periódico ISSN {args.issn} via ArticleMeta...', file=sys.stderr)
        resultados = buscar_articlemeta_por_issn(args.issn, max_resultados=args.max)
    else:
        print(f'🔎 Busca por texto não tem endpoint estruturado público. Tentando search frontend...', file=sys.stderr)
        resultados = buscar_scielo_search(args.query, max_resultados=args.max)
        if not resultados:
            print('💡 Sugestão: use --issn de um periódico específico para resultados estruturados.', file=sys.stderr)
            print('💡 Para busca por texto livre, use o navegador em https://search.scielo.org', file=sys.stderr)
            sys.exit(0)

    print(f'✅ {len(resultados)} resultados.\n', file=sys.stderr)

    if args.json_out:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
        return

    for i, art in enumerate(resultados, 1):
        print(f'--- {i} ---')
        print(f"Título: {art.get('titulo', '')}")
        print(f"Autores: {', '.join(art.get('autores', []))}")
        print(f"Periódico: {art.get('periodico', '')} ({art.get('ano', '')})")
        if art.get('doi'):
            print(f"DOI: {art['doi']}")
        if args.abnt:
            print(f"\nReferência ABNT:\n{formatar_referencia_abnt(art)}")
        print()


if __name__ == '__main__':
    main()
