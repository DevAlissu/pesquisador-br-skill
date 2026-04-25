# Template: Planilha de Extração de Dados

> Estrutura padronizada de extração para revisões sistemáticas e integrativas.

## Modelo de planilha (CSV / Excel / Google Sheets)

### Aba 1: Identificação e elegibilidade

| ID | Autores | Ano | Título | Periódico | Qualis | DOI | Idioma | Selecionado por título? | Selecionado por resumo? | Selecionado por texto completo? | Motivo exclusão |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | Silva, A.; Costa, B. | 2022 | Título | Rev BR Ed | A1 | 10.xxx | PT | Sim | Sim | Sim | — |
| 002 | Pereira | 2021 | ... | ... | B2 | ... | ... | Sim | Não | — | População diferente |
| ... | | | | | | | | | | | |

### Aba 2: Características dos estudos incluídos

| ID | Autores | Ano | País | Tipo estudo | Delineamento | População | Tamanho amostral | Intervenção/Variável | Comparador | Desfecho primário | Período de coleta |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | Silva | 2022 | Brasil | Empírico | Estudo de caso | Estudantes universitários | 80 | Ensino híbrido | Presencial | Desempenho acadêmico | 2020-2021 |

### Aba 3: Procedimentos metodológicos

| ID | Instrumento de coleta | Procedimento de análise | Ferramenta software | Aspectos éticos (CAAE) |
|---|---|---|---|---|
| 001 | Questionário Likert | ANOVA | SPSS 25 | CAAE 12345 |

### Aba 4: Achados e qualidade

| ID | Achado principal | Achado secundário | Limitações reportadas | Risco de viés (instrumento) | Nota qualidade | Observações revisor |
|---|---|---|---|---|---|---|
| 001 | Aumento de 15% no desempenho | Maior satisfação | Amostra pequena | Cochrane RoB: alguns | 7/10 | Bem desenhado |

### Aba 5: Categorização temática

| ID | Eixo temático 1 | Eixo temático 2 | Eixo temático 3 | Tópico emergente |
|---|---|---|---|---|
| 001 | Engajamento | Tecnologia educacional | Aprendizagem ativa | Hibridização emergencial |

## Boas práticas

### Antes de extrair
1. **Valide a planilha** com 2-3 estudos piloto antes de iniciar a extração formal
2. **Treine os revisores**: revisem juntos os 5 primeiros estudos
3. **Calcule concordância**: Kappa ≥ 0,80 indica boa concordância

### Durante a extração
1. **Dupla extração**: 2 revisores independentes
2. **Resolva discordâncias**: consenso ou terceiro revisor
3. **Documente decisões**: por que excluiu cada estudo

### Após a extração
1. **Confira dados** ausentes
2. **Padronize unidades** (médias, percentis, intervalos de confiança)
3. **Identifique outliers** (estudos com valores muito diferentes)

## Ferramentas recomendadas

### Gratuitas
- **Rayyan** (https://rayyan.ai) — triagem por dois revisores
- **Mendeley** — gestão de referências
- **Zotero** — gestão de referências
- **Google Sheets** — planilha colaborativa

### Pagas
- **Covidence** (https://www.covidence.org) — RS Cochrane
- **EndNote** — gestão de referências
- **DistillerSR** — RS robusta

### Análise estatística (metanálise)
- **R** + pacote `metafor` (gratuito, recomendado)
- **RevMan** (Cochrane, gratuito)
- **CMA — Comprehensive Meta-Analysis** (pago)
- **Stata** com módulo `metaan`

## Como reportar

Na seção **Métodos** do paper:

```
A extração foi realizada em planilha Google Sheets estruturada
em [N] aba(s), contendo os seguintes campos: [...]. Dois
pesquisadores extraíram os dados de forma independente,
com confronto e resolução de discordâncias por consenso. A
concordância inter-avaliadores foi medida pelo coeficiente
Kappa de Cohen (κ = 0.85, considerada substancial segundo
Landis e Koch, 1977).
```

## Cuidados

❌ Não confie em **memória** — sempre na planilha
❌ Não **modifique** dados extraídos sem registrar (track changes)
❌ Não **omita** estudos que vão contra sua hipótese
❌ Não **redondeie** valores estatísticos sem critério explícito
✅ **Backup** da planilha em diferentes locais (Drive, GitHub privado, HD)
