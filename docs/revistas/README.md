# Documentação Revistas Qualis A — pesquisador-br-skill

> Esta pasta é um **índice** dos arquivos da skill sobre revistas científicas BR Qualis A por área. O conteúdo completo fica em [`skills/pesquisador-br/references/revistas/`](../../skills/pesquisador-br/references/revistas/), pra ser carregado pela skill em runtime.

## Áreas cobertas

| Área CAPES | Arquivo | Inclui |
|---|---|---|
| **Ciência da Computação** | [`computacao.md`](../../skills/pesquisador-br/references/revistas/computacao.md) | JBCS, JIDM, RBIE, congressos SBC |
| **Educação** | [`educacao.md`](../../skills/pesquisador-br/references/revistas/educacao.md) | Cadernos de Pesquisa, RBE, Educação & Sociedade |
| **Saúde Coletiva** | [`saude-coletiva.md`](../../skills/pesquisador-br/references/revistas/saude-coletiva.md) | CSP, RSP, C&SC |
| **Administração** | [`administracao.md`](../../skills/pesquisador-br/references/revistas/administracao.md) | RAE, RAC, RAUSP, BAR |
| **Engenharias** | [`engenharias.md`](../../skills/pesquisador-br/references/revistas/engenharias.md) | Pesquisa Operacional, Gestão & Produção, IEEE |
| **Direito** | [`direito.md`](../../skills/pesquisador-br/references/revistas/direito.md) | Direito GV, RDA, CONPEDI |
| **Letras / Linguística** | [`letras-linguistica.md`](../../skills/pesquisador-br/references/revistas/letras-linguistica.md) | DELTA, RBLA, ANPOLL |
| **Psicologia** | [`psicologia.md`](../../skills/pesquisador-br/references/revistas/psicologia.md) | Paidéia, Psicologia: T&P, Psico-USF |
| **Serviço Social** | [`servico-social.md`](../../skills/pesquisador-br/references/revistas/servico-social.md) | Serviço Social & Sociedade, Katálysis, Temporalis |

## Como a skill usa

Quando o usuário diz "quero publicar um artigo na minha área", a skill:
1. Pergunta **qual a área CAPES**
2. Carrega o arquivo correspondente da pasta `revistas/`
3. Sugere revistas adequadas ao **estrato Qualis** do usuário
4. Indica **eventos relevantes** (anais com Qualis)
5. Adverte sobre **revistas predatórias** (Beall's List)

## Áreas ainda não cobertas

Áreas com cobertura **futura prevista**:
- Antropologia / Arqueologia
- Sociologia
- História
- Geografia
- Filosofia / Teologia
- Economia
- Ciência Política / Relações Internacionais
- Comunicação e Informação
- Artes
- Medicina I, II, III
- Enfermagem
- Farmácia
- Odontologia
- Ciências Biológicas (I, II, III)
- Ciências Agrárias
- Ciências Ambientais

⚠️ Contribuições de PRs com revistas dessas áreas são **muito bem-vindas**. Veja [`docs/CONTRIBUINDO.md`](../CONTRIBUINDO.md).

## Fontes

- [Plataforma Sucupira (Qualis oficial)](https://sucupira.capes.gov.br)
- [Documentos de Área CAPES](https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao)
- [Beall's List](https://beallslist.net) — cuidado com revistas predatórias
- [SciELO Brasil](https://www.scielo.br)
