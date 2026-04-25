# Arquitetura — pesquisador-br-skill

Como o projeto é estruturado e por quê.

---

## Visão geral

```
pesquisador-br-skill/
│
├── .claude-plugin/              # Manifests do plugin Claude Code
│   ├── marketplace.json
│   └── plugin.json
│
├── docs/                        # Documentação do projeto
│   ├── INSTALACAO.md
│   ├── USO.md
│   ├── ARQUITETURA.md
│   ├── CONTRIBUINDO.md
│   ├── abnt/README.md           # Índice -> skills/.../references/abnt/
│   ├── qualis/README.md         # Índice -> skills/.../references/qualis/
│   ├── plataformas/README.md    # Índice -> skills/.../references/plataformas/
│   ├── metodologia/README.md    # Índice -> skills/.../references/metodologia/
│   └── revistas/README.md       # Índice -> skills/.../references/revistas/
│
├── skills/                      # Skills do plugin
│   ├── pesquisador-br/          # Skill principal (orquestrador)
│   ├── revisao-sistematica-br/  # PRISMA-PT, integrativa, scoping
│   ├── revisor-pares-br/        # Peer review estilo Qualis
│   └── tcc-abnt/                # TCC graduação completo
│
├── scripts/                     # Utilitários Python (stdlib only)
│   ├── busca_scielo.py          # ArticleMeta API por ISSN
│   ├── busca_bdtd.py            # OAI-PMH (UFRGS Lume + outros)
│   ├── doi_para_referencia.py   # CrossRef -> ABNT 6023
│   ├── valida_referencias.py    # Heurística de formato ABNT
│   └── verifica_qualis.py       # Guia de consulta Sucupira
│
├── .github/workflows/           # CI/CD
│   └── ci.yml                   # Validação de estrutura
│
├── README.md                    # Apresentação do projeto
├── LICENSE                      # MIT
└── .gitignore
```

---

## Por que essa arquitetura?

### Princípio 1: Modularidade
Cada skill tem responsabilidade única e pode ser usada independentemente.

- `pesquisador-br` é o **orquestrador**: skill mais ampla, lida com tudo.
- `revisao-sistematica-br` é **especializada**: invocada apenas quando RS é o foco.
- `revisor-pares-br` é **especializada**: invocada quando o foco é peer review.
- `tcc-abnt` é **focada**: pra TCC de graduação completo.

### Princípio 2: Separação de conhecimento e ação
Cada skill tem:
- `SKILL.md`: persona + protocolo + comportamento
- `agents/`: agentes secundários invocados conforme contexto
- `templates/`: estruturas prontas
- `references/`: bases de conhecimento (NBR, Qualis, autores, plataformas)
- `examples/`: exemplos reais de uso

### Princípio 3: Conhecimento explícito
Toda regra ABNT, todo protocolo, toda referência canônica está **escrito em markdown** acessível ao Claude. Sem código mágico, sem dependência de modelo treinado em conhecimento BR.

### Princípio 4: Reusabilidade
- Templates são .md genéricos que o Claude preenche
- Scripts Python são utilities standalone (sem dependências)
- Documentação cruza-referencia (links internos)

---

## Estrutura de uma skill (padrão)

```
skills/pesquisador-br/
│
├── SKILL.md                     # Frontmatter + persona + protocolo
│
├── agents/                      # Agentes especializados (12)
│   ├── intake.md                # Triagem inicial
│   ├── pesquisador-base.md      # Define expertise da área CAPES
│   ├── revisor-literatura.md    # Busca em bases BR
│   ├── arquiteto-estrutura.md   # Escolhe template + monta sumário
│   ├── argumentador.md          # Tese, hipóteses, contribuição
│   ├── escritor-rascunho.md     # Escrita seção por seção
│   ├── revisor-abnt.md          # Conferência de NBR 6023/10520
│   ├── citacao-verificador.md   # Auditoria citação ↔ referência
│   ├── revisor-pares.md         # Simulação de revisor Qualis
│   ├── formatador-final.md      # Aplica NBR 14724
│   ├── mentor-socratico.md      # Modo professor (explica)
│   └── tradutor-bilingue.md     # Resumo PT + Abstract EN
│
├── templates/                   # Templates de documentos
│   ├── artigo-imrad-pt-br.md
│   ├── tcc-completo.md
│   ├── monografia.md
│   ├── dissertacao-mestrado.md
│   ├── tese-doutorado.md
│   ├── projeto-pesquisa-cnpq.md
│   ├── projeto-fapesp.md
│   ├── revisao-sistematica-prisma-pt.md
│   ├── revisao-integrativa.md
│   ├── metanalise.md
│   ├── parecer-academico.md
│   ├── relatorio-pibic.md
│   ├── resposta-revisor.md
│   └── latex/
│       ├── abntex2-tcc.tex
│       ├── abntex2-dissertacao.tex
│       ├── abntex2-tese.tex
│       ├── sbc-artigo.tex
│       └── anped-trabalho.tex
│
└── references/                  # Bases de conhecimento
    ├── abnt/
    │   ├── nbr-6022-artigos.md
    │   ├── nbr-6023-referencias.md
    │   ├── nbr-6024-numeracao.md
    │   ├── nbr-6027-sumario.md
    │   ├── nbr-6028-resumos.md
    │   ├── nbr-6034-indices.md
    │   ├── nbr-10520-citacoes.md
    │   ├── nbr-12225-lombada.md
    │   ├── nbr-14724-trabalhos.md
    │   └── nbr-15287-projetos.md
    ├── qualis/
    │   ├── areas-capes.md
    │   ├── estratos.md
    │   └── como-consultar.md
    ├── plataformas/
    │   ├── lattes.md
    │   ├── scielo.md
    │   ├── periodicos-capes.md
    │   ├── bdtd.md
    │   ├── sucupira.md
    │   └── cnpq-cv-grupos.md
    ├── metodologia/
    │   ├── autores-classicos-br.md
    │   ├── tipos-pesquisa.md
    │   ├── prisma-pt.md
    │   ├── analise-conteudo-bardin.md
    │   └── revisao-integrativa-botelho.md
    ├── revistas/
    │   ├── computacao.md
    │   ├── educacao.md
    │   ├── saude-coletiva.md
    │   ├── administracao.md
    │   ├── direito.md
    │   ├── engenharias.md
    │   ├── psicologia.md
    │   ├── letras-linguistica.md
    │   └── servico-social.md
    └── portugues-academico/
        ├── impessoalidade.md
        ├── conectivos.md
        ├── erros-comuns.md
        └── tempo-verbal.md
```

⚠️ Pasta `examples/` ainda não existe — está prevista para v0.3.0 (exemplos reais anonimizados).

---

## Ciclo de vida de uma interação

```
1. Usuário envia mensagem no Claude Code
   ↓
2. Claude detecta trigger (ex: "ABNT", "TCC", "Qualis")
   ↓
3. Claude carrega SKILL.md da skill correspondente
   ↓
4. Claude lê o frontmatter + protocolo
   ↓
5. Claude executa o intake (perguntas iniciais)
   ↓
6. Conforme a etapa, Claude carrega:
   - agents/<agente-relevante>.md
   - templates/<template-aplicável>.md
   - references/<conhecimento-necessário>.md
   ↓
7. Claude responde ao usuário, mantendo o protocolo
   ↓
8. Iteração até integrity gate ou conclusão
```

---

## Princípios técnicos

### 1. Anti-alucinação
- **Política "Real Citations Only"**: zero tolerância a referências fabricadas
- Quando incerto, Claude **diz explicitamente** ao usuário e pede verificação
- Scripts Python (`doi_para_referencia.py`, `busca_scielo.py`) reduzem dependência de memória do modelo

### 2. Integrity Gates
Pontos do pipeline em que Claude **não avança** sem ter verificado:
- Toda citação tem fonte real?
- Não há plágio?
- Estrutura ABNT está conforme?
- Disclosure de IA foi feita (se aplicável)?

### 3. Calibração contextual
SKILL.md sempre pergunta:
- Área CAPES (49 áreas)
- Tipo de trabalho (TCC, dissertação, etc)
- Qualis alvo (A1-B4)
- Etapa do trabalho

→ Adapta tom, vocabulário, profundidade.

### 4. Voz do pesquisador
- Português acadêmico impessoal (passiva sintética)
- Anti-floreio
- Anti-coloquialismo
- Conectivos cultos
- Critério metodológico real

### 5. Devil's Advocate
Claude **discorda** se o usuário propor metodologia frágil. Não aprova só pra ser agradável.

---

## Por que sintetizar das 3 skills internacionais?

| Inspiração | O que pegamos |
|---|---|
| `academic-research-skills` (Imbad0202) | Pipeline 10-stage com integrity gates, Devil's Advocate, Material Passport |
| `claude-scientific-writer` (K-Dense-AI) | Templates múltiplos por venue, scripts Python reais, real citations only |
| `claude-scholar` (Galaxy-Dawn) | Engenharia de installer, hooks, multi-CLI support, organização modular de skills |

E adicionamos:
- ✅ NBR ABNT completas (única)
- ✅ Qualis CAPES por área (única)
- ✅ Plataformas BR (Lattes, SciELO, CAPES, BDTD, Sucupira) (única)
- ✅ Autores canônicos BR (Gil, Marconi, Minayo, Bardin) (única)
- ✅ Revistas top BR por área (única)
- ✅ Português acadêmico real (única)
- ✅ Templates ABNT (TCC, dissertação, tese, projeto CNPq) (única)
- ✅ PRISMA-PT (única)

---

## Decisões de design

### Por que markdown e não JSON/YAML pra templates?
- Markdown é legível pelo Claude e pelo humano
- Permite estrutura semântica (headers, listas)
- Editável sem ferramenta especial

### Por que Python e não Node?
- Python é universalmente disponível em ambientes acadêmicos
- Scripts são utility, não core; usuário pode rodar manualmente
- Não introduz dependência de runtime

### Por que MIT e não CC-BY-NC?
- Maximiza adoção
- Permite uso comercial (consultorias, agências)
- Acompanha padrão do ecossistema Claude Code (`claude-scientific-writer` e `claude-scholar` também são MIT)

### Por que estrutura de plugin (`.claude-plugin/`)?
- Padrão emergente do Claude Code
- Permite instalação via marketplace
- Compatível com PluginListEntry do Claude

### Por que skills separadas (4) em vez de uma só?
- Cada skill tem trigger único (não confunde Claude)
- Permite invocação direta pra casos específicos
- Mais fácil de manter (cada skill tem dono cognitivo)

---

## Onde adicionar contribuições

### Templates novos
→ `skills/pesquisador-br/templates/`

Exemplo: `templates/parecer-bnq-graduacao.md` (parecer de Banca de Qualificação de Doutorado).

### NBR nova ou atualizada
→ `skills/pesquisador-br/references/abnt/`

Quando sair NBR nova (ex: NBR 14724:2025), criar `nbr-14724-2025.md` e linkar do SKILL.md.

### Revistas de área não coberta
→ `skills/pesquisador-br/references/revistas/`

Exemplo: `references/revistas/teologia.md`, `references/revistas/musica.md`.

### Autor canônico de área
→ `skills/pesquisador-br/references/metodologia/autores-classicos-br.md`

Adicionar nova seção com obras + quando citar.

### Script utilitário
→ `scripts/`

Exemplo: `scripts/busca_lattes.py`, `scripts/extrai_anais_sbc.py`.

### Skill nova focada
→ `skills/<nome-novo>/`

Exemplo: `skills/projeto-fapesp-completo/`, `skills/redacao-cientifica-engenharias/`.

---

## Roadmap

### v0.1.0 (entregue)
- [x] Estrutura base do plugin
- [x] Skill `pesquisador-br` core
- [x] NBR 6023, 10520, 14724
- [x] Templates: TCC, artigo IMRaD, projeto CNPq
- [x] Qualis + autores canônicos
- [x] Scripts SciELO + DOI
- [x] Skill `revisao-sistematica-br`
- [x] Documentação básica

### v0.2.0 (atual — abr/2026)
- [x] Skill `revisor-pares-br` completa
- [x] Skill `tcc-abnt` completa (com 5 templates de capítulo)
- [x] Templates LaTeX (`.tex`) com abnTeX2 + ANPEd + SBC
- [x] NBRs 6022, 6024, 6027, 6028, 6034, 12225, 14724, 15287
- [x] References de revistas em 9 áreas CAPES
- [x] Scripts: SciELO, BDTD via OAI-PMH, DOI/CrossRef, validação ABNT
- [ ] Hooks (auto-revisão ABNT antes de finalizar)
- [ ] CLI standalone (`pesquisador-br` no terminal)

### v0.3.0 (próximo)
- [ ] Pasta `examples/` com casos reais anonimizados
- [ ] Cobertura de revistas em mais áreas (Antropologia, Sociologia, História, etc)
- [ ] Geração de figuras (Mermaid, TikZ, PGFPlots)
- [ ] Metanálise: scripts R/Python pra forest plot
- [ ] Suporte a mais idiomas (espanhol acadêmico hispanofalante)

### v1.0.0 (estável)
- [ ] Cobertura completa de todas as áreas CAPES
- [ ] Validação por pesquisadores brasileiros (banca de validação)
- [ ] Publicação em paper acadêmico (sobre a própria skill como ferramenta)
- [ ] Curso online integrado
