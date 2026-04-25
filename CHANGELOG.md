# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [0.1.0] — 2026-04-25

Primeira versão pública. Plugin Claude Code com **4 skills**, **12 agentes**, **14 templates**, **5 templates LaTeX**, **10 NBRs ABNT documentadas** e **5 scripts Python**, todos focados em pesquisa acadêmica brasileira.

### ✨ Skills

- **`pesquisador-br`** — pipeline completo de 10 etapas para artigo, TCC, dissertação, tese ou projeto, com 12 agentes especializados (intake, pesquisador-base, revisor-literatura, arquiteto-estrutura, argumentador, escritor-rascunho, revisor-abnt, citacao-verificador, revisor-pares, formatador-final, mentor-socratico, tradutor-bilingue) e 10 modos de operação (`full`, `plan`, `outline-only`, `revision`, `revision-coach`, `abstract-only`, `lit-review`, `format-convert`, `citation-check`, `disclosure`).
- **`revisao-sistematica-br`** — RS PRISMA-PT 2020, integrativa Botelho et al. e scoping (Arksey & O'Malley) com 6 templates (protocolo RS, protocolo integrativa, extração de dados, diagrama PRISMA, RoB 2, relatório PRISMA).
- **`revisor-pares-br`** — simulação de revisor Qualis A1-B2 em 6 dimensões (originalidade, fundamentação, metodologia, resultados, escrita, ABNT).
- **`tcc-abnt`** — pipeline focado em TCC de graduação com 5 templates de capítulo (introdução, referencial, metodologia, resultados, considerações finais).

### 📚 Normas ABNT documentadas

- NBR 6022:2018 — Artigos em periódicos
- NBR 6023:2018 — Referências
- NBR 6024:2012 — Numeração progressiva
- NBR 6027:2012 — Sumário
- NBR 6028:2021 — Resumo, resenha e recensão
- NBR 6034:2004 — Índice
- NBR 10520:2023 — Citações
- NBR 12225:2004 — Lombada
- NBR 14724:2011 — Trabalhos acadêmicos
- NBR 15287:2011 — Projetos de pesquisa

### 🎓 Bases de conhecimento

- **Qualis CAPES**: 49 áreas, 9 estratos (A1-C), guia passo-a-passo Sucupira
- **Plataformas BR**: Lattes, SciELO, Periódicos CAPES (CAFe), BDTD, Sucupira, CNPq (DGP + bolsas)
- **Metodologia**: autores canônicos BR (Gil, Marconi & Lakatos, Minayo, Bardin, Triviños, Yin, Demo, Thiollent), tipos de pesquisa (4 eixos), PRISMA-PT, Análise de Conteúdo (Bardin), revisão integrativa (Botelho et al.)
- **Revistas Qualis A** em 9 áreas: Computação, Educação, Saúde Coletiva, Administração, Engenharias, Direito, Letras/Linguística, Psicologia, Serviço Social
- **Português acadêmico**: impessoalidade (passiva sintética), conectivos cultos por função, erros frequentes (crase, regência), tempo verbal por seção

### 📝 Templates de trabalho

- Artigo IMRaD adaptado PT-BR
- TCC graduação completo
- Monografia (especialização lato sensu)
- Dissertação (mestrado)
- Tese (doutorado)
- Projeto de pesquisa CNPq/CAPES
- Projeto FAPESP / FAPs estaduais
- Revisão sistemática PRISMA-PT
- Revisão integrativa (Botelho)
- Meta-análise (PRISMA + Cochrane + GRADE)
- Parecer acadêmico ad hoc
- Carta de resposta a revisor (R&R)
- Relatório PIBIC/PIBITI

### 🎨 Templates LaTeX

- `abntex2-tcc.tex`, `abntex2-dissertacao.tex`, `abntex2-tese.tex`
- `sbc-artigo.tex` (computação)
- `anped-trabalho.tex` (educação)

### 🐍 Scripts Python (zero dependências)

- `busca_scielo.py` — consulta SciELO via ArticleMeta API por ISSN
- `busca_bdtd.py` — coleta de teses via OAI-PMH (UFRGS Lume default; aliases para USP, UFMG, BDTD)
- `doi_para_referencia.py` — DOI → referência ABNT 6023 via CrossRef
- `valida_referencias.py` — validação heurística de formato ABNT 6023
- `verifica_qualis.py` — guia interativo de consulta Qualis na Sucupira

### 🛡️ Segurança

- **Anti-SSRF em `busca_bdtd.py`**: bloqueia esquemas não-http(s), IPs literais loopback/link-local/privados/multicast/reservados, IPv4-mapped IPv6 (`::ffff:127.0.0.1`), 6to4 wrappings, hostnames que resolvem para IPs locais (DNS rebinding via `lvh.me` etc), e revalidação em redirects HTTP (`SafeRedirectHandler`).
- **Anti-prompt-injection no `pesquisador-br/SKILL.md`**: 7 itens em runtime que orientam o modelo a tratar texto/documento/URL/output-de-script como **dado**, nunca **comando**, e reportar `INSTRUÇÃO:` embutida em metadados de terceiros (OAI-PMH, WebFetch).
- **Política Anti-Plágio + Integrity Gate**: bloqueia entrega se houver citação sem fonte, fabricação ou plágio detectado.
- **CI hardening**: GitHub Actions pinadas por SHA, `permissions: contents: read` declarado.
- **Zero dependências externas** nos scripts (apenas stdlib do Python 3.9+).

### ⚠️ Limitação conhecida

- `busca_bdtd.py --endpoint <url>`: passe apenas URLs de repositórios institucionais conhecidos. A validação anti-SSRF cobre os vetores comuns (file://, loopback, IPv4-mapped, DNS rebinding via getaddrinfo, redirect chain), mas não elimina TOCTOU (atacante mudando o registro DNS entre a validação e a request real). Recomendado usar os aliases internos: `--endpoint ufrgs|usp|ufmg|bdtd`. Mitigação completa de TOCTOU planejada para v0.2.0.

### 🧪 Cobertura de testes

- **Golden test** em CI: `formatar_referencia_abnt` em `busca_scielo.py`
- **Auto-test** `valida_referencias.py --teste`: 13 casos (5 referências completas + 8 de `tem_cidade_editora`)
- **Auto-test** `busca_bdtd.py --teste`: 29 casos (`validar_endpoint` com 4 OK + 14 reject + 2 DNS rebinding + `_extrair_ano` + `formatar_autor_abnt`)
- **Auto-test** `doi_para_referencia.py --teste`: 13 casos (`formatar_abnt` com 1 autor / 4+ autores / meta=None + sanitização de prefixos URL)

### 📖 Documentação

- README com instalação, quick-start e estrutura
- INSTALACAO.md (3 métodos: marketplace, manual, link simbólico)
- USO.md com 7 exemplos reais (TCC zero, conversão APA→ABNT, RS, revisão de texto, R&R, verificação Qualis, disclosure de IA)
- ARQUITETURA.md detalhando estrutura, princípios e roadmap
- CONTRIBUINDO.md com padrões, code of conduct e seção anti-prompt-injection para mantenedores
- 5 índices em `docs/{abnt,qualis,plataformas,metodologia,revistas}/README.md`

### 🤝 Inspirações

Sintetizada a partir de:
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — pipeline 10-stage e integrity gates
- [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) — templates de venues e scripts Python
- [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) — engenharia de installer e organização modular

Adaptada e expandida para realidade brasileira (ABNT, Qualis CAPES, plataformas nacionais).

### 🇧🇷 Compatibilidade

- **Claude Code** (CLI, web app `claude.ai/code`, IDE extensions): suporte nativo via `/plugin marketplace add`
- **Outras ferramentas** (Aider, Cursor, Cline, Continue.dev): conteúdo é markdown/Python plain — utilizável manualmente referenciando os arquivos do repositório

---

[0.1.0]: https://github.com/DevAlissu/pesquisador-br-skill/releases/tag/v0.1.0
