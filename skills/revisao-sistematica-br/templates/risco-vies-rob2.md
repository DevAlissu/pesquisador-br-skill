# Template: Avaliação de Risco de Viés (RoB 2 e alternativas)

> Avaliação de qualidade metodológica dos estudos primários incluídos na revisão.

## Por tipo de estudo

| Tipo | Ferramenta recomendada |
|---|---|
| **Ensaios clínicos randomizados** | Cochrane RoB 2 |
| **Estudos observacionais** (coorte, caso-controle) | Newcastle-Ottawa Scale (NOS) |
| **Estudos qualitativos** | CASP / JBI Critical Appraisal |
| **Revisões sistemáticas** (overview) | AMSTAR-2 |
| **Estudos diagnósticos** | QUADAS-2 |
| **Estudos econômicos** | Drummond Checklist |

## Cochrane RoB 2 (RCTs)

5 domínios, cada um classificado como **baixo / preocupações / alto** risco:

### Domínio 1: Viés decorrente do processo de randomização
- A sequência de randomização foi gerada aleatoriamente?
- A alocação foi ocultada?
- As características dos grupos eram comparáveis no início?

### Domínio 2: Viés devido a desvios das intervenções pretendidas
- Os participantes ficaram cegados?
- Profissionais que aplicaram a intervenção foram cegados?
- Houve aderência ao protocolo planejado?

### Domínio 3: Viés devido a dados ausentes
- Os dados estavam disponíveis para todos (≥ 95%) ou quase todos os participantes?
- A ausência foi relacionada ao desfecho?

### Domínio 4: Viés na medição do desfecho
- O método de medição foi adequado?
- Avaliadores estavam cegados?
- A mensuração foi consistente entre os grupos?

### Domínio 5: Viés na seleção do resultado reportado
- Os resultados estavam pré-especificados?
- O resultado reportado é fiel ao planejado?

### Risco geral
- **Baixo**: todos os domínios baixos
- **Algumas preocupações**: pelo menos 1 domínio com preocupações
- **Alto**: pelo menos 1 domínio alto

## Newcastle-Ottawa Scale (NOS) — observacionais

8 itens em 3 categorias (cada item vale 0-1 estrela, total 0-9):

### Seleção (0-4 estrelas)
1. Representatividade dos casos: ⭐
2. Seleção dos controles: ⭐
3. Verificação dos casos: ⭐
4. Demonstração de que o desfecho não estava presente no início: ⭐

### Comparabilidade (0-2 estrelas)
5. Comparabilidade dos grupos (controle de confundidores): ⭐⭐

### Resultado (0-3 estrelas)
6. Avaliação do desfecho: ⭐
7. Tempo de seguimento adequado: ⭐
8. Adequação da taxa de seguimento (≥ 85%): ⭐

### Interpretação
- **0-3 estrelas**: alto risco
- **4-6 estrelas**: moderado
- **7-9 estrelas**: baixo risco

## CASP — Estudos qualitativos

10 perguntas SIM / NÃO / NÃO CLARO:

1. Os objetivos foram claramente declarados?
2. A metodologia qualitativa é apropriada?
3. O desenho da pesquisa é apropriado para o objetivo?
4. A estratégia de amostragem é adequada?
5. A coleta de dados é detalhada?
6. A relação pesquisador-participante foi considerada?
7. Aspectos éticos foram contemplados?
8. A análise foi rigorosa?
9. Os achados são claramente apresentados?
10. A pesquisa é valiosa?

### Interpretação
- 9-10 SIM: alto rigor
- 7-8 SIM: moderado
- ≤ 6 SIM: baixo rigor

## AMSTAR-2 — Revisões sistemáticas

16 itens com diferentes níveis de criticalidade. Resultado:
- **Alto**: 0 falhas críticas, 0-1 não-críticas
- **Moderado**: 0 falhas críticas, várias não-críticas
- **Baixo**: 1 falha crítica
- **Criticamente baixo**: > 1 falha crítica

## Como reportar

### Tabela resumida

| ID | Autor | Ano | Tipo | Ferramenta | Resultado | Notas |
|---|---|---|---|---|---|---|
| 001 | Silva | 2022 | RCT | RoB 2 | Baixo | — |
| 002 | Costa | 2021 | Coorte | NOS | 8/9 | Baixo |
| 003 | Pereira | 2020 | Qualitativo | CASP | 9/10 | Alto rigor |
| 004 | Souza | 2019 | RCT | RoB 2 | Algumas preocupações | Cegamento |

### Visualização

Ferramentas que geram visualizações:
- **robvis** (R package): https://github.com/mcguinlu/robvis
- **Cochrane RevMan**: gera plot oficial
- **Excel + condicional**: cores por domínio

## Apresentação no texto

```
3.5 Avaliação do risco de viés

Adotou-se o instrumento Cochrane RoB 2 para avaliação dos
ensaios clínicos randomizados (HIGGINS et al., 2019). Para
estudos observacionais, utilizou-se a Newcastle-Ottawa Scale
(WELLS et al., 2014). A avaliação foi realizada de forma
independente por dois pesquisadores, com resolução de
discordâncias por consenso. A concordância inter-avaliadores
foi κ = 0.82 (substancial).

Resultados (Quadro 2):
- Baixo risco: 18 estudos (39%)
- Algumas preocupações: 22 estudos (48%)
- Alto risco: 6 estudos (13%)

Análise de sensibilidade foi realizada excluindo estudos com
alto risco de viés.
```

## Análise de sensibilidade

⚠️ **Recomendado**: refazer a metanálise (se aplicável) excluindo
estudos com alto risco de viés. Se os resultados mudam
significativamente, reportar e discutir.

## Cuidados

✅ Use a ferramenta apropriada para o tipo de estudo
✅ Avaliação por DOIS revisores
✅ Reporte concordância (Kappa)
✅ Seja transparente: liste cada decisão
✅ Faça análise de sensibilidade

❌ Inventar avaliações
❌ Excluir estudos só porque têm alto risco de viés (incluir, mas reportar)
❌ Misturar ferramentas para o mesmo tipo de estudo
