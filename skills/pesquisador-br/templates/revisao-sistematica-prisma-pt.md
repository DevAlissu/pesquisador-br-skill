# Template: Revisão Sistemática (PRISMA-PT)

> Estrutura para revisão sistemática seguindo PRISMA 2020 (versão portuguesa).
> Adaptado para revistas brasileiras Qualis A.

## 📋 Estrutura PRISMA 2020 (27 itens)

```
TÍTULO
1. Título identificando o trabalho como revisão sistemática

RESUMO
2. Resumo estruturado: (a) background; (b) objectives;
   (c) methods; (d) results; (e) conclusions; (f) systematic review
   registration

INTRODUÇÃO
3. Justificativa
4. Objetivos (com PICO/PICOC explícito)

MÉTODOS
5. Critérios de elegibilidade
6. Fontes de informação (bases consultadas)
7. Estratégia de busca (strings completas)
8. Processo de seleção dos estudos
9. Processo de extração de dados
10. Lista de itens dos dados extraídos
11. Avaliação do risco de viés dos estudos individuais
12. Medidas de efeito
13. Métodos de síntese
14. Avaliação do viés de publicação (se aplicável)
15. Avaliação da certeza/qualidade da evidência (GRADE, se aplicável)

RESULTADOS
16. Seleção dos estudos (incluir diagrama PRISMA)
17. Características dos estudos
18. Risco de viés nos estudos
19. Resultados individuais
20. Resultados das sínteses
21. Resultados sobre vieses adicionais

DISCUSSÃO
22. Discussão geral
23. Limitações da evidência
24. Limitações dos processos da revisão
25. Implicações

OUTROS
26. Registro e protocolo
27. Suporte (financiamento)
```

## Modelo preenchido

```markdown
# REVISÃO SISTEMÁTICA — [Título da revisão]

## RESUMO ESTRUTURADO

**Contexto**: [Por que essa revisão é importante? Qual a lacuna?]

**Objetivo**: [Pergunta PICO ou PICOC]

**Métodos**: Foram consultadas as bases SciELO Brasil, Periódicos
CAPES, BDTD, Cochrane Library e PubMed em [data]. Os critérios
de inclusão foram: (i) [...]; (ii) [...]; (iii) [...]. A análise
seguiu PRISMA 2020.

**Resultados**: A busca identificou [N] artigos. Após triagem
por título/resumo e leitura de texto completo, [N] estudos foram
incluídos. [Síntese dos achados]

**Conclusões**: [Síntese da evidência]

**Registro**: PROSPERO [nº]

**Palavras-chave**: revisão sistemática; [tema]; PRISMA;
metanálise; evidência baseada em pesquisa.

---

## 1 INTRODUÇÃO

### 1.1 Contextualização

[Apresentação do tema, fundamentação da relevância da revisão]

### 1.2 Justificativa para a revisão sistemática

A presente revisão se justifica por: (i) [evidência da lacuna];
(ii) [revisões prévias e o que ainda falta]; (iii) [potencial
contribuição prática].

### 1.3 Objetivo

**Pergunta PICO**:
- **P** (População/Problema): [descrição]
- **I** (Intervenção/Indicador): [descrição]
- **C** (Comparação): [descrição]
- **O** (Outcome/Desfecho): [descrição]

**Objetivo geral**: Sistematizar evidências disponíveis sobre
[tema] em [contexto].

**Objetivos específicos**:
(a) Identificar [...];
(b) Comparar [...];
(c) Sintetizar [...].

---

## 2 MÉTODOS

### 2.1 Protocolo e registro

O protocolo desta revisão foi registrado em PROSPERO sob o nº
[CRD420XXXXX] em [data]. A revisão segue as recomendações do
PRISMA 2020.

### 2.2 Critérios de elegibilidade

**Inclusão**:
- Artigos completos peer-reviewed
- Período: 2014-2024
- Idiomas: PT, EN, ES
- Tipo de estudo: ensaios clínicos, estudos observacionais,
  estudos de caso (especificar)
- População: [população]
- Intervenção: [intervenção]

**Exclusão**:
- Resumos, editoriais, opiniões
- Artigos sem texto completo disponível
- Estudos com [critério de exclusão específico]

### 2.3 Fontes de informação

Foram consultadas as seguintes bases:
1. **SciELO Brasil** — https://search.scielo.org
2. **Portal de Periódicos CAPES** — Scopus + Web of Science
3. **BDTD/IBICT** — https://bdtd.ibict.br
4. **Cochrane Library** (se saúde)
5. **PubMed/MEDLINE** (se saúde)
6. **Google Scholar** (literatura cinzenta)

Data de busca: [data].

### 2.4 Estratégia de busca

**SciELO Brasil** (PT-BR):
```
("[termo principal]" OR "[sinônimo 1]") AND ("[termo 2]" OR "[sinônimo]")
```

**Scopus** (EN):
```
TITLE-ABS-KEY (("term1" OR "synonym") AND ("term2" OR "synonym"))
AND PUBYEAR > 2013
```

**PubMed**:
```
("[MeSH term]"[MeSH] OR "[free text]"[Title/Abstract]) AND
("[MeSH term 2]"[MeSH])
Filters: 2014-2024, Humans
```

[Repetir pra cada base com strings completas]

### 2.5 Processo de seleção

A triagem ocorreu em três fases:
1. **Identificação**: total de registros
2. **Triagem por título e resumo**: dois revisores independentes
3. **Avaliação de elegibilidade (texto completo)**: dois revisores

Discordâncias foram resolvidas por consenso ou consulta a um
terceiro revisor. A concordância inter-avaliadores foi medida
pelo coeficiente Kappa de Cohen.

### 2.6 Processo de extração de dados

Os dados foram extraídos em planilha estruturada contendo:
- Identificação do estudo (autores, ano, periódico, país)
- Característica metodológica (delineamento, amostra, instrumento)
- Achados principais
- Risco de viés
- Limitações reportadas

A extração foi realizada de forma independente por dois
pesquisadores, com confronto e consenso.

### 2.7 Avaliação do risco de viés

Adotou-se [ferramenta]:
- **Cochrane RoB 2** (ensaios clínicos randomizados)
- **NOS** (Newcastle-Ottawa Scale, observacionais)
- **JBI Critical Appraisal** (estudos qualitativos)
- **AMSTAR-2** (revisões sistemáticas)

### 2.8 Síntese dos resultados

**Síntese qualitativa** (narrativa): organização por eixos
temáticos, articulação dos achados.

**Síntese quantitativa** (metanálise): cálculo de tamanho de
efeito (RR, OR, d de Cohen), heterogeneidade (I²),
forest plot — quando ≥ 3 estudos com dados comparáveis.

### 2.9 Avaliação da certeza da evidência

Adotou-se a ferramenta **GRADE** (Grading of Recommendations
Assessment, Development and Evaluation) para avaliar a certeza
da evidência por desfecho.

---

## 3 RESULTADOS

### 3.1 Seleção dos estudos

A busca identificou [N] registros nas bases consultadas. Após
remoção de duplicatas, foram triados [N] resumos. Após leitura
completa, [N] estudos foram incluídos. O fluxograma PRISMA é
apresentado na Figura 1.

**Figura 1 - Fluxograma PRISMA 2020**

```
[IDENTIFICAÇÃO]
SciELO: 145 / Scopus: 312 / WoS: 198 / BDTD: 67 / Total: 722
Após remoção de duplicatas: 524

[TRIAGEM]
Resumos triados: 524
Excluídos por título/resumo: 412
Avaliados em texto completo: 112

[ELEGIBILIDADE]
Excluídos por critérios:
  - Não atendem população: 28
  - Não atendem intervenção: 19
  - Sem texto completo: 11
  - Outros: 8
Total excluído: 66

[INCLUSÃO]
Estudos incluídos: 46
```

### 3.2 Características dos estudos

A Tabela 1 apresenta as características dos [N] estudos
incluídos.

[Tabela com colunas: Autores (ano), país, delineamento, amostra,
instrumento, achado principal]

### 3.3 Risco de viés

[Análise do risco de viés conforme ferramenta adotada]

### 3.4 Resultados das sínteses

[Síntese qualitativa por eixos temáticos OU metanálise com
forest plot]

---

## 4 DISCUSSÃO

### 4.1 Síntese da evidência

[Discussão dos achados em relação à literatura prévia]

### 4.2 Limitações da evidência incluída

[Limitações dos estudos primários — ex: amostras pequenas,
heterogeneidade, viés de publicação]

### 4.3 Limitações da revisão

[Limitações do processo da revisão — ex: idiomas excluídos,
período curto, bases consultadas]

### 4.4 Implicações

**Para a prática**: [...]
**Para a pesquisa**: [...]
**Para políticas**: [...]

---

## 5 CONCLUSÕES

[Síntese conclusiva da revisão]

---

## REGISTRO E PROTOCOLO

Esta revisão foi registrada em PROSPERO sob o nº [CRD420XXXXX].
O protocolo está disponível em [URL].

## CONFLITOS DE INTERESSE

Os autores declaram não haver conflito de interesse.

## FINANCIAMENTO

Esta revisão recebeu apoio da [agência] sob o processo nº [...].

## DISCLOSURE DE IA (se aplicável)

[Declaração conforme padrão]

## REFERÊNCIAS

[Lista NBR 6023 — incluindo todos os estudos primários +
referências da metodologia]
```

## Recursos adicionais

- **Checklist PRISMA 2020 PT**: https://prisma-statement.org/Translations/Translations
- **Diagrama PRISMA gerador**: https://estech.shinyapps.io/prisma_flowdiagram/
- **PROSPERO** (registro): https://www.crd.york.ac.uk/PROSPERO/

## Checklist final

- [ ] Pergunta PICO/PICOC explícita
- [ ] Protocolo registrado em PROSPERO antes de iniciar
- [ ] Strings de busca completas em cada base
- [ ] Triagem por dois revisores independentes
- [ ] Coeficiente Kappa reportado
- [ ] Diagrama PRISMA com números detalhados
- [ ] Tabela de características dos estudos
- [ ] Avaliação de risco de viés
- [ ] Síntese qualitativa OU quantitativa (metanálise)
- [ ] Limitações declaradas
- [ ] Disclosure de IA
- [ ] Referências NBR 6023
