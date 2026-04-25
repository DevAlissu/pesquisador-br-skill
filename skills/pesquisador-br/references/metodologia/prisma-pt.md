# PRISMA-PT 2020 — Revisão Sistemática

> *Preferred Reporting Items for Systematic Reviews and Meta-Analyses* — em português, **2020**.

PRISMA é o **padrão internacional** para reportar revisões sistemáticas. A versão 2020 (revisão da 2009) é a vigente e foi traduzida pra PT-BR.

---

## O que é uma Revisão Sistemática

Pesquisa **secundária** que segue protocolo rigoroso pra:
- Identificar **toda** a evidência sobre uma pergunta específica
- Selecionar com critérios pré-definidos
- Avaliar a **qualidade metodológica**
- Sintetizar (qualitativa ou quantitativa-meta-análise)

Diferente de revisão narrativa: rigor, replicabilidade, transparência.

---

## Etapas obrigatórias (PRISMA 2020)

### 1. **Pergunta de pesquisa estruturada (PICO/PICOS/PECO)**

Estruture a pergunta:

| Sigla | Significado | Exemplo (saúde) | Exemplo (educação) |
|---|---|---|---|
| **P** | População / Problema | Idosos hipertensos | Estudantes EaD |
| **I** | Intervenção / Exposição | Caminhada 30min/dia | Gamificação |
| **C** | Comparação / Controle | Cuidado padrão | Aula tradicional |
| **O** | Outcome (desfecho) | Pressão arterial | Engajamento |
| **S** | Study design | RCT | Quasi-experimental |

### 2. **Protocolo registrado** (PROSPERO)

Antes de começar, **registre o protocolo** em:
- **PROSPERO**: https://www.crd.york.ac.uk/prospero (saúde, principalmente)
- **OSF Registries**: https://osf.io/registries (geral)

⚠️ Registrar **antes** evita "dredge"/cherry-picking de resultados.

### 3. **Bases de busca e estratégia**

Mínimo recomendado: **3-5 bases**.

| Base | Foco |
|---|---|
| PubMed/MEDLINE | Saúde |
| Web of Science | Multidisciplinar |
| Scopus | Multidisciplinar |
| Cochrane | Saúde, ensaios |
| LILACS / SciELO | Latam, BR |
| ERIC | Educação |
| ACM / IEEE Xplore | Computação |
| EMBASE | Farmácia, saúde |

### Estratégia de busca
- **Termos MeSH/DeCS** + **palavras-chave**
- **Operadores booleanos** (AND, OR, NOT)
- **Filtros**: idioma, ano, tipo de estudo

Exemplo (saúde):
```
("hypertension"[MeSH] OR "high blood pressure")
AND ("exercise"[MeSH] OR "physical activity")
AND (trial[pt] OR randomized[ti])
```

### 4. **Critérios de inclusão e exclusão**

#### Inclusão
- Tipo de estudo (RCT, observacional, qualitativo)
- Período (ex: 2014-2024)
- Idioma (PT, EN, ES)
- População específica (PICO)
- Acesso ao texto completo

#### Exclusão
- Resumos de eventos
- Editoriais, cartas, opiniões
- Estudos sem dados primários
- Duplicatas

### 5. **Seleção dos estudos (3 fases)**

| Fase | Filtro |
|---|---|
| **1. Identificação** | Importar todas as referências (Rayyan, Mendeley) |
| **2. Triagem** | Ler título e resumo |
| **3. Elegibilidade** | Ler texto completo |

⚠️ **Dois revisores independentes** em cada fase. Discordâncias resolvidas por terceiro revisor.

Ferramentas:
- **Rayyan** (https://rayyan.ai) — gratuito, cega revisores
- **Covidence** (pago, completo)
- **EPPI-Reviewer** (pago, robusto)

### 6. **Diagrama PRISMA 2020 (fluxograma)**

```
┌──────────────────────────────┐
│ IDENTIFICAÇÃO                │
│ Bases (n=...)                │
│ Outras fontes (n=...)        │
│ Total: n=...                 │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ TRIAGEM (n=...)              │
│ Excluídos por título/resumo  │
│ (n=..., razões)              │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ ELEGIBILIDADE (n=...)        │
│ Excluídos por texto completo │
│ (n=..., razões detalhadas)   │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ INCLUÍDOS NA SÍNTESE (n=...) │
│ - Síntese qualitativa: n=... │
│ - Meta-análise: n=...        │
└──────────────────────────────┘
```

Templates: http://www.prisma-statement.org

### 7. **Extração de dados**

Tabela padronizada com:
- Autor + ano
- País / contexto
- População (n, idade, gênero)
- Intervenção
- Comparação
- Desfechos (medidas, resultados)
- Limitações

Use planilha (Google Sheets, Excel) com pelo menos 2 revisores.

### 8. **Avaliação da qualidade / risco de viés**

Por **tipo de estudo**:

| Tipo | Ferramenta |
|---|---|
| **RCT** | RoB 2 (Cochrane) |
| **Observacional** | Newcastle-Ottawa Scale, ROBINS-I |
| **Quali** | CASP, SRQR |
| **Misto** | MMAT (Mixed Methods Appraisal Tool) |

⚠️ Reporte **sempre** o risco de viés — alto, médio, baixo.

### 9. **Síntese**

#### Qualitativa
- Síntese narrativa estruturada
- Tabelas comparativas
- Análise temática

#### Quantitativa (meta-análise)
- Forest plot
- Funnel plot (viés de publicação)
- Heterogeneidade (I², Q de Cochran)
- Modelo de efeitos fixos vs aleatórios
- Software: RevMan, STATA, R (`metafor`)

### 10. **Reporte (Checklist PRISMA 2020)**

Reporte **27 itens** obrigatórios:
1. Título indica RS
2. Resumo estruturado (PICO + métodos + resultados)
3. Justificativa
4. Objetivos
5. Critérios de elegibilidade
6. Bases consultadas
7. Estratégia de busca completa (apêndice)
8. Processo de seleção
9. Processo de extração
10. Lista de itens extraídos
11. Avaliação de risco de viés
12. Métodos de síntese
13. ... (lista completa em http://www.prisma-statement.org/PRISMAStatement/Checklist.aspx)
14. Resultados da seleção (com diagrama)
15. Características dos estudos
16. Risco de viés
17. Síntese
18. Discussão
19. Limitações
20. Conclusões
21. Conflitos de interesse
22. Apoio financeiro
23. Disponibilidade dos dados

---

## Tipos de revisão (não confunda)

| Tipo | Pergunta | Tempo | Rigor |
|---|---|---|---|
| **Sistemática** | Específica | 6-12 meses | PRISMA |
| **Rápida** | Específica, urgente | 4-8 semanas | Adaptado |
| **Meta-análise** | Específica + sintetizar quanti | 6-12 meses | PRISMA + Cochrane |
| **Integrativa** | Híbrida (quali + quanti) | 3-6 meses | Botelho et al. |
| **Escopo (scoping)** | Mapeamento amplo | 3-6 meses | PRISMA-ScR |
| **Narrativa** | Discutir tema | 1-3 meses | Sem protocolo |
| **Estado da arte** | Estado atual da literatura | 1-3 meses | Adaptado |

⚠️ Pra cada tipo, há um manual:
- **Sistemática**: Cochrane Handbook
- **Integrativa**: Botelho et al. (2011)
- **Scoping**: Arksey & O'Malley (2005), JBI Manual

Ver `revisao-integrativa-botelho.md` para o método de Botelho et al.

---

## Erros frequentes

❌ Sem **registro de protocolo** (PROSPERO/OSF) — não é RS sem isso
❌ **Estratégia de busca** mal documentada (ninguém replica)
❌ **Apenas uma base** (insuficiente)
❌ **Apenas um revisor** (não cega)
❌ **Sem avaliação de qualidade**
❌ **Sem diagrama PRISMA 2020** (fluxograma)
❌ Confundir com **revisão narrativa**
❌ Apenas resumos, sem texto completo
❌ Excluir estudos por **resultado** (cherry-picking)

---

## Boas práticas

✅ **Registre protocolo** antes de começar
✅ **Use 2+ revisores** independentes
✅ **Combine 3-5 bases** mínimo
✅ **Use Rayyan** ou Covidence pra triagem
✅ **Diagrama PRISMA 2020** sempre
✅ **Avalie risco de viés** com ferramenta apropriada
✅ **Reporte os 27 itens** do checklist PRISMA
✅ **Triangule** com revisão manual de listas de referências dos incluídos

---

## Fonte oficial PRISMA 2020 (PT-BR)

PAGE, Matthew J. *et al.* The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, [s.l.], v. 372, p. n71, 2021. DOI: 10.1136/bmj.n71.

Tradução PT:
PAGE, Matthew J. *et al.* A declaração PRISMA 2020: diretriz atualizada para relatar revisões sistemáticas. *Revista Panamericana de Salud Pública*, [s.l.], v. 46, e112, 2022. DOI: 10.26633/RPSP.2022.112.

---

## Recursos

- [PRISMA Statement Oficial](http://www.prisma-statement.org)
- [PRISMA 2020 Flow Diagram (gerador)](https://estech.shinyapps.io/prisma_flowdiagram/)
- [Cochrane Handbook](https://training.cochrane.org/handbook)
- [PROSPERO Registry](https://www.crd.york.ac.uk/prospero)
- [OSF Registries](https://osf.io/registries)
- [Rayyan (triagem)](https://rayyan.ai)
- [JBI Manual](https://jbi-global-wiki.refined.site)
