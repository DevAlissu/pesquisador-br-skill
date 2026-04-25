# Template — Meta-análise

> Para revisões sistemáticas que **sintetizam quantitativamente** os resultados de estudos primários. Padrão **PRISMA 2020** + **Cochrane Handbook**.

## Quando usar

✅ Pergunta de pesquisa **específica**
✅ Estudos primários **homogêneos** (mesmo desenho — RCT, observacional)
✅ Desfecho **mensurável** quantitativamente (média, proporção, razão)
✅ Mínimo de **5-10 estudos** elegíveis
✅ Dados estatísticos suficientes (média, DP, n; ou OR, RR, IC95%)

❌ **Não use** quando:
- Estudos qualitativos (use síntese narrativa ou meta-ethnography)
- Estudos muito heterogêneos
- Poucos estudos primários (< 5)
- Dados incompletos / inconsistentes

---

## Estrutura do trabalho

```
1 INTRODUÇÃO
2 REFERENCIAL TEÓRICO
3 METODOLOGIA
   3.1 Pergunta e estrutura PICO
   3.2 Critérios de inclusão e exclusão
   3.3 Estratégia de busca
   3.4 Seleção dos estudos
   3.5 Extração de dados
   3.6 Avaliação do risco de viés
   3.7 Síntese estatística (meta-análise)
   3.8 Avaliação da heterogeneidade
   3.9 Análise de sensibilidade e subgrupos
4 RESULTADOS
   4.1 Fluxo de seleção (diagrama PRISMA)
   4.2 Caracterização dos estudos incluídos
   4.3 Risco de viés
   4.4 Síntese quantitativa (forest plot)
   4.5 Heterogeneidade
   4.6 Análise de sensibilidade
   4.7 Viés de publicação (funnel plot)
5 DISCUSSÃO
6 CONCLUSÕES
REFERÊNCIAS
APÊNDICES
```

---

## 3.1 Pergunta de pesquisa (PICO)

```
P (População): [definição]
I (Intervenção): [definição]
C (Comparação): [definição, se aplicável]
O (Outcome / Desfecho): [definição com unidade de medida]
```

Exemplo:
```
P: Idosos com hipertensão arterial leve
I: Atividade física aeróbica regular (≥150 min/semana)
C: Cuidado padrão sem intervenção sistemática
O: Pressão arterial sistólica (mmHg) após 12 semanas
```

⚠️ Quanto **mais específica** a pergunta, mais robusta a meta-análise.

---

## 3.2 Critérios de inclusão e exclusão

### Inclusão
- **Tipo de estudo**: ensaio clínico randomizado (RCT) / quasi-experimental / coorte
- **População**: [especificar]
- **Intervenção**: [especificar]
- **Comparação**: [especificar]
- **Desfecho**: [com unidade]
- **Período**: últimos N anos
- **Idiomas**: PT, EN, ES
- **Texto completo disponível**

### Exclusão
- Estudos com dados incompletos
- Estudos duplicados (manter o mais recente)
- Editoriais, cartas, opiniões
- Estudos sem grupo controle (se RCT é o critério)
- Estudos com população fora do PICO

---

## 3.3 Estratégia de busca

### Bases (mínimo 5)
- PubMed/MEDLINE
- Embase
- Cochrane Library / CENTRAL
- LILACS / SciELO
- Web of Science ou Scopus

### Termos
**MeSH/DeCS** + **palavras-chave** + **operadores booleanos**:

```
("hypertension"[MeSH] OR "high blood pressure")
AND ("exercise"[MeSH] OR "physical activity")
AND ("randomized controlled trial"[pt] OR randomized[ti])
AND (older[ti] OR elderly[ti] OR aged[MeSH])
```

⚠️ Documentar **a estratégia completa** no apêndice (transparência PRISMA).

---

## 3.5 Extração de dados

Tabela mestra:

| ID | Autor + ano | País | n (I/C) | Idade média | Intervenção | Duração | Desfecho I | Desfecho C | Diferença média | DP | Risco de viés |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | Silva, 2020 | BR | 30/30 | 68 | Caminhada 30min/dia | 12 sem | 130 mmHg | 138 mmHg | -8 | 5,2 | Baixo |
| E2 | Souza, 2021 | EUA | 45/45 | 72 | Hidroginástica | 16 sem | 128 | 140 | -12 | 6,1 | Baixo |
| ... | | | | | | | | | | | |

⚠️ **Dois revisores independentes** extraem; discordâncias resolvidas por terceiro.

---

## 3.6 Avaliação do risco de viés

### Por tipo de estudo

| Tipo | Ferramenta |
|---|---|
| **RCT** | RoB 2 (Cochrane) |
| **Não-randomizado** | ROBINS-I |
| **Observacional** | Newcastle-Ottawa Scale |
| **Acurácia diagnóstica** | QUADAS-2 |

⚠️ Apresente como **gráfico** (semáforo: verde-amarelo-vermelho) ou **tabela**.

---

## 3.7 Síntese estatística

### Modelos
- **Efeitos fixos** (FE): assume verdadeiro efeito comum
- **Efeitos aleatórios** (RE): assume distribuição de efeitos (mais comum)

⚠️ Heterogeneidade alta (I² > 50%) → use **efeitos aleatórios** sempre.

### Medidas de efeito

#### Para variáveis contínuas
- **Diferença média (MD)**: quando todos os estudos usam a mesma escala
- **Diferença média padronizada (SMD)**: quando escalas variam (Cohen's d)

#### Para variáveis dicotômicas
- **Risk Ratio (RR)** ou **Razão de Risco**
- **Odds Ratio (OR)** ou **Razão de Chances**
- **Hazard Ratio (HR)** para análise de sobrevivência

### Software
- **RevMan** (Cochrane, gratuito) — RCTs e revisões clássicas
- **STATA** com módulos `meta`, `metan`, `metafor`
- **R** com pacote `metafor` ou `meta`
- **CMA** (Comprehensive Meta-Analysis) — pago, mas robusto

---

## 3.8 Heterogeneidade

### Estatísticas
- **I²**: % da variância devido a heterogeneidade
  - <25%: baixa
  - 25-50%: moderada
  - 50-75%: substancial
  - >75%: considerável
- **Q de Cochran**: teste de heterogeneidade (p < 0,10 = heterogeneidade)
- **τ²**: variância entre estudos

### O que fazer com I² alto?
1. **Análise de subgrupos** (por idade, sexo, dose, etc)
2. **Meta-regressão** (variável quantitativa)
3. **Restringir** a estudos mais homogêneos
4. **Síntese narrativa** se muito alta

---

## 4.4 Forest plot (apresentação principal)

```
Estudo (n)         Efeito (IC95%)        |  ← favorece I  |  → favorece C
-----              --------------         |               |
Silva 2020 (60)    -8.0 (-12.5, -3.5)    |    ████ |
Souza 2021 (90)   -12.0 (-16.2, -7.8)    |  ████  |
Lima 2022 (75)     -7.5 (-11.0, -4.0)    |    ████ |
Costa 2023 (120)  -10.5 (-13.8, -7.2)    |   ████ |
Mendes 2024 (88)   -9.0 (-13.5, -4.5)    |    ████ |
-----              --------------         |               |
Pooled            -9.5 (-11.7, -7.3)     |     ◆◆        |  Heterogeneidade: I² = 32%
                                          |               |
                  -20  -15  -10   -5   0   5   10  (mmHg)
```

⚠️ Inclua sempre:
- Effect size com IC 95%
- Tamanho do quadrado proporcional ao peso do estudo
- Diamante representando o efeito conjunto (pooled)
- Estatísticas de heterogeneidade abaixo

---

## 4.7 Funnel plot (viés de publicação)

```
Erro padrão
    0 ┌─────────────●─────────────┐
      │            ●●●            │
      │          ●●●●●            │
      │        ●●●●●●●            │
      │     ●●●●●●●●●●            │
    1 │                            │
      └────────────────────────────┘
                Effect size
```

⚠️ **Funnel plot simétrico** = sem viés de publicação.
**Assimétrico** = sugere viés.

Testes formais:
- **Egger's test** (regressão)
- **Begg's test** (correlação)

p < 0,10 = sugere viés.

---

## Avaliação GRADE

⚠️ **Recomendado em revistas top**: classifica a **qualidade da evidência**.

| Nível | Significado |
|---|---|
| **Alta** | Confiança alta — pesquisas futuras improvávelmente mudarão |
| **Moderada** | Confiança média — pesquisas futuras podem mudar |
| **Baixa** | Confiança baixa — pesquisas futuras provavelmente mudarão |
| **Muito baixa** | Estimativa muito incerta |

Fatores que **rebaixam**:
- Risco de viés alto
- Inconsistência (heterogeneidade)
- Indireto (PICO não bate)
- Imprecisão (IC amplo)
- Viés de publicação

---

## Reporte (PRISMA 2020 — 27 itens)

⚠️ Submeta junto com o **checklist PRISMA preenchido** (apêndice).

URL: http://www.prisma-statement.org/PRISMAStatement/Checklist.aspx

---

## Erros frequentes

❌ **Combinar** estudos com PICOs muito diferentes
❌ **Ignorar heterogeneidade** alta
❌ Não fazer **análise de sensibilidade**
❌ Não avaliar **viés de publicação**
❌ Não registrar protocolo no PROSPERO
❌ Apenas **um revisor** na seleção/extração
❌ Sem **diagrama PRISMA**
❌ Sem **GRADE** (em revisões top)
❌ Mistura unidades (mmHg + kPa, kg + lb)
❌ Não converter dados quando necessário (mediana → média via fórmula)

---

## Boas práticas

✅ **Registre o protocolo** no PROSPERO antes de começar
✅ **Use 2+ revisores** independentes
✅ **Documente a estratégia** completa (apêndice)
✅ **Forest + funnel plots** sempre
✅ **GRADE** se for área biomédica
✅ **Análise de sensibilidade**
✅ **Reporte os 27 itens PRISMA**
✅ **Compartilhe dados** (OSF, Mendeley Data)

---

## Tempo médio

- Protocolo: 1-2 meses
- Busca + triagem: 2-4 meses
- Extração + análise: 2-3 meses
- Redação: 2-3 meses
- **Total**: 8-12 meses (em equipe de 2-3)

---

## Recursos

- [PRISMA 2020](http://www.prisma-statement.org)
- [Cochrane Handbook](https://training.cochrane.org/handbook)
- [PROSPERO](https://www.crd.york.ac.uk/prospero)
- [GRADE](https://www.gradeworkinggroup.org)
- [RevMan](https://training.cochrane.org/online-learning/core-software/revman)
- [metafor (R)](https://www.metafor-project.org)
- Ver `references/metodologia/prisma-pt.md`
- Ver `references/metodologia/revisao-integrativa-botelho.md`
