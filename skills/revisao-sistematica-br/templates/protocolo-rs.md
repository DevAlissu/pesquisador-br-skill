# Template: Protocolo de Revisão Sistemática

> Documento que **antecede** a revisão. Registra critérios e procedimentos antes de executar a busca.
> Equivalente brasileiro ao registro PROSPERO.

## Cabeçalho

```markdown
# PROTOCOLO DE REVISÃO SISTEMÁTICA

**Título da revisão**: [título]
**Pesquisadores**: [nomes + filiação]
**Data do protocolo**: [data]
**Versão**: 1.0
**Registro PROSPERO**: [CRD420XXXXX, se já registrado]
```

## Estrutura

### 1. Justificativa

[Por que esta revisão é necessária? Qual a lacuna na literatura?]

### 2. Pergunta de pesquisa (PICO/PICOC)

- **P** (População): [...]
- **I** (Intervenção): [...]
- **C** (Comparação): [...]
- **O** (Outcome): [...]
- **C** (Contexto, opcional): [...]

**Pergunta consolidada**: [...]?

### 3. Objetivos

**Geral**: Sistematizar a evidência sobre [tema] em [contexto].

**Específicos**:
1. Identificar [...]
2. Comparar [...]
3. Sintetizar [...]

### 4. Critérios de elegibilidade

#### Inclusão
- Tipo de estudo: [ensaios clínicos randomizados / estudos observacionais / qualitativos / etc]
- População: [...]
- Intervenção: [...]
- Período: [ano1] a [ano2]
- Idiomas: PT, EN, ES
- Disponibilidade: texto completo

#### Exclusão
- Editoriais, opiniões, cartas
- Resumos sem texto completo
- Estudos com [característica específica]
- Duplicatas

### 5. Fontes de informação

| Base | URL | Cobertura |
|---|---|---|
| SciELO Brasil | https://search.scielo.org | PT-BR open access |
| Scopus (via CAPES) | https://www.scopus.com | Multi-disciplinar |
| Web of Science | https://www.webofscience.com | Multi-disciplinar |
| BDTD/IBICT | https://bdtd.ibict.br | Teses BR |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | Saúde |
| Cochrane | https://www.cochranelibrary.com | Saúde, RS |

### 6. Estratégia de busca

**SciELO** (PT-BR):
```
("[principal]" OR "[sinônimo]") AND ("[principal2]" OR "[sinônimo2]")
```

**Scopus** (EN):
```
TITLE-ABS-KEY (("term1" OR "synonym") AND ("term2" OR "synonym"))
AND PUBYEAR > 2013 AND ( LIMIT-TO ( DOCTYPE,"ar" ) )
```

**PubMed**:
```
("[MeSH]"[MeSH] OR "[free text]"[Title/Abstract]) AND
("[MeSH 2]"[MeSH])
Filters: 2014-2024, Humans
```

[Replicar para cada base]

### 7. Processo de seleção

**Fase 1 — Triagem por título e resumo**
- Dois revisores independentes
- Tool: Rayyan (gratuito) ou Covidence
- Concordância calculada por Kappa de Cohen

**Fase 2 — Avaliação de elegibilidade (texto completo)**
- Dois revisores independentes
- Resolver discordâncias por consenso ou terceiro revisor

### 8. Extração de dados

**Tool**: planilha estruturada (Excel ou Google Sheets) com campos:

| Campo | Descrição |
|---|---|
| ID estudo | Sequencial |
| Autores (ano) | Citação completa |
| País | Local do estudo |
| Periódico | Nome + Qualis |
| Tipo de estudo | Delineamento |
| Amostra | N + descrição |
| Intervenção | Descrição |
| Comparador | Se houver |
| Desfecho primário | Métrica |
| Desfecho secundário | Métrica |
| Achado principal | Síntese 2-3 frases |
| Risco de viés | Resultado da avaliação |
| Limitações reportadas | Pelos próprios autores |

### 9. Avaliação do risco de viés

| Tipo de estudo | Ferramenta |
|---|---|
| Ensaios clínicos randomizados | Cochrane RoB 2 |
| Estudos observacionais | NOS (Newcastle-Ottawa) |
| Estudos qualitativos | CASP / JBI |
| Revisões sistemáticas | AMSTAR-2 |

### 10. Síntese

**Qualitativa** (sempre): organização por eixos temáticos.

**Quantitativa** (se aplicável): metanálise se ≥ 3 estudos com
dados comparáveis.
- Tamanho de efeito: [Risco Relativo / Odds Ratio / d de Cohen]
- Heterogeneidade: I²
- Forest plot
- Análise de subgrupo: por [variável]

### 11. Avaliação da certeza da evidência

GRADE (Grading of Recommendations Assessment) por desfecho:
- **Alta**: pesquisa robusta, sem inconsistências
- **Moderada**: limitações pequenas
- **Baixa**: limitações importantes
- **Muito baixa**: limitações críticas

### 12. Cronograma do protocolo

| Etapa | Mês 1-2 | Mês 3-4 | Mês 5-6 | Mês 7-8 |
|---|---|---|---|---|
| Registro PROSPERO | ✅ | | | |
| Strings + busca | | ✅ | | |
| Triagem | | | ✅ | |
| Extração + análise | | | ✅ | ✅ |
| Síntese + redação | | | | ✅ |

### 13. Equipe

| Pesquisador | Função |
|---|---|
| [Nome] | Coordenador, revisor 1 |
| [Nome] | Revisor 2 |
| [Nome] | Terceiro revisor (resolver discordâncias) |
| [Nome] | Estatístico (se metanálise) |

### 14. Conflitos de interesse

[Declaração]

### 15. Financiamento

[Agência financiadora se houver]

### 16. Referências do protocolo

- HIGGINS, J. P. T. *et al.* **Cochrane Handbook for Systematic Reviews of Interventions**. London: Cochrane, 2024.
- PAGE, M. J. *et al.* The PRISMA 2020 statement. *BMJ*, v. 372, n. 71, 2021. DOI: 10.1136/bmj.n71.

---

## Checklist de protocolo

- [ ] PICO/PICOC explícito
- [ ] Critérios I/E claros
- [ ] Bases listadas com strings completas
- [ ] Procedimento de triagem detalhado
- [ ] Ferramenta de extração padronizada
- [ ] Risco de viés especificado por tipo de estudo
- [ ] Síntese (narrativa e/ou metanálise) definida
- [ ] Equipe e responsabilidades definidas
- [ ] Cronograma realista
- [ ] Registro PROSPERO antes de iniciar busca
