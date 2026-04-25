# Documentação Plataformas BR — pesquisador-br-skill

> Esta pasta é um **índice** dos arquivos da skill sobre plataformas brasileiras de pesquisa. O conteúdo completo fica em [`skills/pesquisador-br/references/plataformas/`](../../skills/pesquisador-br/references/plataformas/), pra ser carregado pela skill em runtime.

## Plataformas cobertas

| Plataforma | Função | Arquivo |
|---|---|---|
| **Lattes (CNPq)** | Currículos de pesquisadores BR | [`lattes.md`](../../skills/pesquisador-br/references/plataformas/lattes.md) |
| **SciELO** | Revistas BR/Latam open access | [`scielo.md`](../../skills/pesquisador-br/references/plataformas/scielo.md) |
| **Periódicos CAPES** | Acesso CAFe + bases internacionais | [`periodicos-capes.md`](../../skills/pesquisador-br/references/plataformas/periodicos-capes.md) |
| **BDTD (IBICT)** | Teses e dissertações BR | [`bdtd.md`](../../skills/pesquisador-br/references/plataformas/bdtd.md) |
| **Sucupira** | PPGs, Qualis, Documentos de Área | [`sucupira.md`](../../skills/pesquisador-br/references/plataformas/sucupira.md) |
| **CNPq** | DGP + bolsas + Carlos Chagas | [`cnpq-cv-grupos.md`](../../skills/pesquisador-br/references/plataformas/cnpq-cv-grupos.md) |

## Scripts utilitários (em `/scripts`)

A skill também oferece scripts Python que consultam algumas dessas plataformas:

| Script | Plataforma | O que faz |
|---|---|---|
| [`busca_scielo.py`](../../scripts/busca_scielo.py) | SciELO | Consulta via ArticleMeta API por ISSN |
| [`busca_bdtd.py`](../../scripts/busca_bdtd.py) | UFRGS Lume / BDTD | OAI-PMH harvesting |
| [`verifica_qualis.py`](../../scripts/verifica_qualis.py) | Sucupira | Guia de consulta manual |
| [`doi_para_referencia.py`](../../scripts/doi_para_referencia.py) | CrossRef | DOI → ABNT |
| [`valida_referencias.py`](../../scripts/valida_referencias.py) | (local) | Heurística ABNT 6023 |

## Fontes oficiais

- [Plataforma Lattes](https://lattes.cnpq.br)
- [SciELO Brasil](https://www.scielo.br)
- [Portal de Periódicos CAPES](https://www.periodicos.capes.gov.br)
- [BDTD/IBICT](https://bdtd.ibict.br)
- [Plataforma Sucupira](https://sucupira.capes.gov.br)
- [Plataforma Carlos Chagas (CNPq)](https://carloschagas.cnpq.br)
