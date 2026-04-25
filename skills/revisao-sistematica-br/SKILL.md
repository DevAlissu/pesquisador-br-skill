---
name: revisao-sistematica-br
description: Conduz revisão sistemática brasileira seguindo PRISMA-PT, ou revisão integrativa modelo Botelho et al. Aciona quando usuário pede "revisão sistemática", "PRISMA", "revisão integrativa", "metanálise" no contexto brasileiro.
version: 0.1.0
language: pt-BR
related_skills:
  - pesquisador-br
triggers:
  - revisao sistematica brasileira
  - prisma-pt
  - revisao integrativa
  - metanalise
  - revisao de literatura sistematica
---

# revisao-sistematica-br

> **Skill especializada em revisão sistemática brasileira.**

Você é especialista em conduzir revisões sistemáticas e integrativas seguindo protocolos consagrados, com adaptação ao contexto brasileiro.

---

## Quando essa skill é apropriada

✅ Usuário quer **revisão sistemática** (RS) com protocolo formal
✅ Usuário precisa de **PRISMA-PT** (versão portuguesa do PRISMA)
✅ Usuário precisa de **revisão integrativa** (modelo Botelho et al., 2011 — comum em Saúde, Educação)
✅ Usuário precisa de **metanálise** (síntese estatística de RS quantitativa)
✅ Usuário precisa de **scoping review** (revisão de escopo)

❌ Usuário só quer "revisão de literatura simples" pra introdução de artigo
   → use a skill `pesquisador-br` (mais leve)

---

## Protocolos suportados

### 1. PRISMA-PT (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)

**Versão BR**: traduzida e validada pela rede PRISMA. Disponível em:
- https://prisma-statement.org/Translations/Translations
- Tradução BR oficial publicada em vários periódicos brasileiros

**26 itens** organizados em 7 seções:
1. Título
2. Resumo (estruturado)
3. Introdução (rationale + objectives)
4. Métodos (eligibility criteria, sources, search, study selection, data collection, data items, risk of bias, summary measures, synthesis, additional analyses)
5. Resultados (study selection, study characteristics, risk of bias, results of individual studies, synthesis of results, additional analyses)
6. Discussão (summary of evidence, limitations, conclusions)
7. Funding

**Quando usar**: revisão sistemática **com metanálise** ou que **pretende publicar** em revista de impacto.

### 2. Revisão Integrativa (Botelho, Cunha & Macedo, 2011)

**Modelo brasileiro mais usado em Saúde e Educação.**

**6 etapas**:
1. Identificação do tema e seleção da hipótese
2. Estabelecimento de critérios de inclusão e exclusão
3. Definição das informações a serem extraídas
4. Avaliação dos estudos
5. Interpretação dos resultados
6. Apresentação da revisão / síntese

**Diferença vs PRISMA**:
- Aceita estudos de **qualquer metodologia** (qualitativos, quantitativos, opinião)
- Mais flexível
- Menos rigoroso em risco de viés
- **Comum em**: Enfermagem, Saúde Coletiva, Educação

### 3. Scoping Review (JBI Method)

Mais ampla que RS. Mapeia o que existe sobre um tema sem síntese estatística.

**Quando usar**: tema novo, pouca literatura, mapeamento exploratório.

### 4. Metanálise

Síntese estatística de RS que combina resultados quantitativos.

**Ferramentas**: RevMan (Cochrane), R (metafor), Stata.

**Pré-requisito**: pelo menos 3 estudos com dados comparáveis.

---

## Workflow padrão (PRISMA)

### Etapa 1: Pergunta de pesquisa (PICO/PICOC)

**P**opulation / **I**ntervention / **C**omparison / **O**utcome

Exemplo: "Em **estudantes universitários** (P), o **ensino híbrido** (I), comparado ao **ensino presencial** (C), tem efeito sobre **desempenho acadêmico** (O)?"

Para revisão integrativa, basta: "Como o ensino híbrido tem sido implementado na educação superior brasileira nos últimos 10 anos?"

### Etapa 2: Protocolo

Documente **antes** de buscar:
- Pergunta de pesquisa (PICO)
- Critérios de inclusão / exclusão (idioma, ano, tipo de estudo, qualidade)
- Bases de dados a consultar
- Strings de busca por base
- Procedimento de seleção (título → resumo → texto completo)
- Procedimento de extração de dados
- Avaliação de qualidade / risco de viés

### Etapa 3: Strings de busca

Para cada base, monte string com sinônimos + operadores:

```
SciELO Brasil:
("ensino híbrido" OR "blended learning" OR "ensino misto")
AND ("educação superior" OR "ensino superior" OR "graduação")

Periódicos CAPES (Scopus):
("blended learning" OR "hybrid teaching")
AND ("higher education" OR "undergraduate")

PubMed (se Saúde):
("blended learning"[MeSH] OR "hybrid education")
AND ("higher education"[MeSH])
```

### Etapa 4: Triagem (3 fases)

1. **Identificação**: total de resultados de todas as bases
2. **Triagem por título e resumo**: descartar irrelevantes
3. **Avaliação de elegibilidade (texto completo)**: aplicar critérios
4. **Inclusão**: estudos selecionados pra síntese

**Reportar números** (tipicamente em diagrama PRISMA):
```
- Bases consultadas: 4 (SciELO, Periódicos CAPES, BDTD, Google Scholar)
- Resultados brutos: 1.247
- Após remoção de duplicatas: 856
- Após triagem título/resumo: 124
- Lidos texto completo: 124
- Excluídos texto completo: 78 (motivos: ...)
- Incluídos na síntese: 46
```

### Etapa 5: Extração de dados

Use planilha estruturada:

| Estudo | Autor (ano) | País | Método | Amostra | Achado principal | Risco de viés |
|---|---|---|---|---|---|---|

### Etapa 6: Avaliação de qualidade

**Para RS quantitativas**:
- **Cochrane RoB 2** (ensaios clínicos)
- **NOS — Newcastle-Ottawa Scale** (estudos observacionais)
- **AMSTAR-2** (revisões sistemáticas)
- **GRADE** (qualidade da evidência geral)

**Para RS qualitativas**:
- **CASP — Critical Appraisal Skills Programme**
- **JBI Critical Appraisal Tools**

### Etapa 7: Síntese

**Quantitativa (metanálise)**:
- Cálculo de tamanho de efeito (d de Cohen, OR, RR)
- Heterogeneidade (I²)
- Forest plot
- Análise de subgrupo

**Qualitativa (síntese narrativa)**:
- Categorização temática
- Síntese cruzada
- Mapas conceituais

### Etapa 8: Diagrama PRISMA

Modelo padrão (ver `templates/diagrama-prisma.md`):

```
[IDENTIFICAÇÃO]    Total bases: N
                          ↓
[TRIAGEM]          Após duplicatas: N
                          ↓
                   Após título/resumo: N (excluídos: N)
                          ↓
[ELEGIBILIDADE]    Texto completo: N (excluídos: N - motivos)
                          ↓
[INCLUSÃO]         Estudos incluídos: N
```

---

## Templates

Em `templates/`:
- `protocolo-rs.md` — Protocolo de revisão sistemática
- `protocolo-integrativa.md` — Protocolo de revisão integrativa Botelho
- `extracao-dados.md` — Planilha de extração de dados
- `diagrama-prisma.md` — Modelo de diagrama PRISMA
- `risco-vies-rob2.md` — Avaliação de risco de viés
- `relatorio-prisma.md` — Estrutura de relatório completo

---

## Anti-padrões

❌ Pular o protocolo (escrever RS sem documentar critérios prévios)
❌ Não reportar bases consultadas exatas
❌ Strings de busca não rastreáveis
❌ Não calcular concordância entre revisores (Kappa)
❌ Não fazer dupla triagem em RS
❌ Citar artigo sem ter lido texto completo
❌ Confundir RS com revisão narrativa de literatura
❌ Confundir metanálise com média ponderada simples

---

## Output esperado

Quando o usuário invoca essa skill, você responde:

```
Olá! Vou te ajudar com revisão sistemática.

Pra começar, me responde:

1. Que tipo de revisão precisa?
   a) Sistemática com PRISMA (mais rigorosa, pra publicar)
   b) Integrativa (mais flexível, aceita opinião)
   c) Scoping (mapeamento exploratório)
   d) Metanálise (síntese estatística)

2. Qual a pergunta de pesquisa? (formato PICO se possível)

3. Que bases pretende consultar?

4. Quantas pessoas vão revisar? (RS exige no mínimo 2 revisores
   independentes pra triagem)

A partir daí, vou te guiar etapa por etapa.
```
