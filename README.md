# 🇧🇷 pesquisador-br-skill

> **A skill definitiva pra pesquisa acadêmica brasileira no Claude Code.**
> ABNT, Qualis CAPES, Lattes, SciELO, Periódicos CAPES, BDTD — tudo nativo, em português, no padrão real das universidades brasileiras.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-purple)](https://docs.claude.com/en/docs/claude-code/plugins)
[![ABNT](https://img.shields.io/badge/Normas-ABNT-green)](https://www.abnt.org.br)
[![Qualis CAPES](https://img.shields.io/badge/CAPES-Qualis-blue)](https://sucupira.capes.gov.br)
[![PT-BR](https://img.shields.io/badge/idioma-PT--BR-yellow)](https://github.com)

---

## 💡 Por que essa skill?

O ecossistema Claude Code tem skills excelentes pra pesquisa acadêmica — mas **todas em inglês e padrão internacional** (APA, IMRaD, NeurIPS, Nature). Pesquisadores brasileiros precisam de:

- ✅ **Normas ABNT** (NBR 6023, 10520, 14724, 15287, 6028, etc) — formatação real, não aproximação
- ✅ **Qualis CAPES** atualizado por área (49 áreas de avaliação)
- ✅ **Plataformas brasileiras**: Lattes, SciELO, Periódicos CAPES, BDTD, Sucupira, OASISbr
- ✅ **Português acadêmico**: impessoalidade, voz passiva, conectivos, regência culta
- ✅ **Autores-referência BR**: Gil, Marconi & Lakatos, Minayo, Bardin, Triviños, Demo, Thiollent
- ✅ **Estruturas reais**: TCC, monografia, dissertação, tese, projeto CAPES/CNPq/FAPESP
- ✅ **Revistas top por área**: SBC, ANPEd, ABRASCO, ANPAD, ANPOLL...

Essa é a primeira skill 100% BR pro Claude Code. Construída sintetizando o melhor das skills internacionais existentes ([academic-research-skills](https://github.com/Imbad0202/academic-research-skills), [claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer), [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)) e adaptando integralmente pro contexto brasileiro.

---

## 🚀 Quick Start

### Instalação via plugin (recomendado)

```bash
/plugin marketplace add https://github.com/DevAlissu/pesquisador-br-skill
/plugin install pesquisador-br-skill
```

### Instalação manual

```bash
git clone https://github.com/DevAlissu/pesquisador-br-skill.git
cp -r pesquisador-br-skill/skills/* ~/.claude/skills/
```

Depois reinicia o Claude Code. Pronto.

---

## 🎯 O que essa skill faz

### Skills incluídas

| Skill | O que faz | Quando usar |
|---|---|---|
| **`pesquisador-br`** | Pipeline completo de pesquisa+escrita acadêmica BR | Artigo, TCC, dissertação, tese |
| **`revisao-sistematica-br`** | Revisão sistemática com PRISMA-PT | RS pra publicar em periódico Qualis |
| **`revisor-pares-br`** | Revisão por pares estilo Qualis A1-B2 | Auto-revisão antes de submeter |
| **`tcc-abnt`** | Geração de TCC completo no padrão ABNT | TCC de graduação |

### Pipeline de pesquisa (estilo ARS)

```
1. INTAKE          → recebe tema, área, tipo de trabalho
2. PESQUISA        → SciELO, Periódicos CAPES, BDTD, Google Scholar BR
3. REVISÃO LIT     → mapeia o que já foi feito no Brasil + internacional
4. ESTRUTURA       → escolhe formato (IMRaD, TCC, dissertação, projeto)
5. ARGUMENTO       → tese, hipóteses, contribuição original
6. RASCUNHO        → escrita seção por seção (PT-BR acadêmico impessoal)
7. CITAÇÃO ABNT    → NBR 6023 + NBR 10520 (autor-data ou numérico)
8. REVISÃO PARES   → simula avaliador Qualis A1
9. FORMATAÇÃO      → NBR 14724 (margens, fonte, espaçamento, sumário)
10. RESUMO BILÍNGUE→ Resumo PT + Abstract EN (NBR 6028)
```

Cada etapa tem **integrity gate**: pendências são bloqueantes.

---

## 📚 Templates incluídos

### Trabalhos acadêmicos
- `artigo-imrad-pt-br.md` — Artigo científico com IMRaD adaptado PT-BR
- `tcc-completo.md` — TCC graduação (intro / referencial / metodologia / resultados / considerações)
- `monografia.md` — Especialização lato sensu
- `dissertacao-mestrado.md` — Dissertação stricto sensu
- `tese-doutorado.md` — Tese (formato tradicional + por artigos)
- `projeto-pesquisa-cnpq.md` — Projeto pra editais CNPq (Universal, PIBIC)
- `projeto-fapesp.md` — Projeto FAPESP / FAPEAM / FAPERJ etc

### Revisão de literatura
- `revisao-sistematica-prisma-pt.md` — RS com PRISMA traduzido
- `revisao-integrativa.md` — Revisão integrativa modelo Botelho et al.
- `metanalise.md` — Meta-análise quantitativa (PRISMA + Cochrane)

### Documentos institucionais
- `relatorio-pibic.md` — Relatório de PIBIC/PIBITI
- `parecer-academico.md` — Parecer ad hoc
- `resposta-revisor.md` — Carta de resposta a peer review

### LaTeX (templates `.tex` prontos)
- `abntex2-tcc.tex` — Padrão abnTeX2 para TCC
- `abntex2-dissertacao.tex` — Dissertação abnTeX2
- `abntex2-tese.tex` — Tese abnTeX2
- `sbc-artigo.tex` — Artigo padrão SBC (computação)
- `anped-trabalho.tex` — Trabalho padrão ANPEd (educação)

---

## 🛠 Bases de conhecimento (`references/`)

### Normas ABNT (cobertura completa)
- NBR 6022:2018 — Artigos em periódicos
- NBR 6023:2018 — Referências
- NBR 6024:2012 — Numeração progressiva
- NBR 6027:2012 — Sumário
- NBR 6028:2021 — Resumo
- NBR 6034:2004 — Índice
- NBR 10520:2023 — Citações
- NBR 12225:2004 — Lombada
- NBR 14724:2011 — Trabalhos acadêmicos (estrutura, formatação)
- NBR 15287:2011 — Projetos de pesquisa

### Qualis CAPES
- 49 áreas de avaliação
- Estratos A1-A4, B1-B4, C
- Como consultar Qualis atualizado no Sucupira

### Plataformas brasileiras
- Lattes (estrutura + busca + integração ORCID)
- SciELO Brasil
- Portal de Periódicos CAPES (acesso CAFe)
- BDTD/IBICT (teses e dissertações)
- Catálogo de Teses CAPES
- Sucupira (programas, conceitos, Qualis)
- OASISbr / Domínio Público / PePsic / SciELO Saúde Pública

### Metodologia BR
- Autores-referência: Gil, Marconi & Lakatos, Minayo, Bardin, Yin, Triviños, Demo, Thiollent
- Tipos de pesquisa (natureza, abordagem, objetivos, procedimentos)
- Pesquisa-ação, estudo de caso, etnografia, survey, ex-post-facto
- PRISMA-PT, Cochrane, modelo Botelho et al. (revisão integrativa)
- Análise de Conteúdo (Bardin), Análise de Discurso, Hermenêutica-dialética (Minayo)

### Revistas top por área
Curadoria de revistas nacionais Qualis A em pelo menos:
- Computação (SBC + congressos)
- Educação (ANPEd, Cadernos de Pesquisa)
- Saúde Coletiva (Cadernos SP, Ciência & Saúde, ABRASCO)
- Administração (RAE, RAC, RAUSP, BAR — ANPAD)
- Engenharias (Pesquisa Operacional, Gestão & Produção, Production)
- Direito (CONPEDI, Revista Direito GV, Sequência)
- Ensino, Letras, Psicologia, Serviço Social...

### Português acadêmico
- Impessoalidade obrigatória + voz passiva sintética
- Conectivos formais
- Erros frequentes ("a nível de", "enquanto que", crase, regência)
- Tempo verbal por seção
- Dado vs informação, "mesmo" como pronome (desaconselhado)

---

## 🐍 Scripts Python utilitários

```
scripts/
├── busca_scielo.py         # Consulta SciELO via ArticleMeta API (por ISSN)
├── busca_bdtd.py           # Coleta de teses via OAI-PMH (UFRGS Lume + outros)
├── doi_para_referencia.py  # DOI → referência ABNT 6023 (CrossRef)
├── valida_referencias.py   # Validação heurística de formato ABNT 6023
└── verifica_qualis.py      # Guia de consulta Qualis na Sucupira
```

⚠️ Os scripts usam apenas stdlib do Python (zero dependências externas) e endpoints públicos. Não exigem chave de API nem autenticação.

---

## 📖 Documentação

- [`docs/INSTALACAO.md`](docs/INSTALACAO.md) — Guia detalhado de instalação
- [`docs/USO.md`](docs/USO.md) — Como usar com exemplos
- [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) — Como a skill é estruturada
- [`docs/CONTRIBUINDO.md`](docs/CONTRIBUINDO.md) — Como contribuir
- [`docs/abnt/`](docs/abnt/) — Normas ABNT detalhadas
- [`docs/qualis/`](docs/qualis/) — Sistema Qualis CAPES
- [`docs/plataformas/`](docs/plataformas/) — Bases brasileiras
- [`docs/metodologia/`](docs/metodologia/) — Metodologia científica BR
- [`docs/revistas/`](docs/revistas/) — Revistas top por área

---

## 🤝 Contribuindo

Essa skill é da comunidade brasileira de pesquisa, pra comunidade brasileira de pesquisa.

Contribuições super bem-vindas:
- Templates por área específica
- Atualização de Qualis quando sair novo quadriênio
- Adição de revistas
- Ajustes de NBRs quando saírem revisões
- Tradução de docs para outros idiomas (espanhol, inglês)

Manda PR ou abre issue.

---

## 🛡️ Segurança

Para reportar vulnerabilidades, veja [`SECURITY.md`](SECURITY.md). **Não abra issue pública** para problemas de segurança — use [GitHub Security Advisories](https://github.com/DevAlissu/pesquisador-br-skill/security/advisories/new) ou e-mail privado.

## 📜 Histórico de versões

Veja [`CHANGELOG.md`](CHANGELOG.md).

## 📄 Licença

MIT — uso livre comercial e acadêmico, com atribuição. Veja [`LICENSE`](LICENSE).

---

## 🙏 Créditos

Inspirada e sintetizada a partir de:
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — pipeline 10-stage e integrity gates
- [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) — templates de venues e scripts Python
- [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) — engenharia de installer e hooks

Adaptada e expandida pra realidade brasileira.

**Construída por:** [DevAlissu](https://github.com/DevAlissu)

---

## 🇧🇷 Vamos descolonizar a pesquisa no Brasil

Você tá fazendo pesquisa em PT-BR sob normas ABNT seguindo critérios CAPES/CNPq. Sua ferramenta deveria saber disso. Agora ela sabe.
