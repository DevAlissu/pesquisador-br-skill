# Template: Projeto de Pesquisa (CNPq / CAPES / FAPs)

> Estrutura para projeto de pesquisa em editais brasileiros (Universal CNPq, FAPESP, FAPEAM, FAPERJ, FAPEMIG, etc).
> Conforme NBR 15287:2011.

---

## 📋 Estrutura padrão

```
1. CAPA (com identificação completa)
2. RESUMO (com palavras-chave)
3. INTRODUÇÃO
   3.1 Apresentação do tema
   3.2 Problema de pesquisa
   3.3 Justificativa
4. OBJETIVOS
   4.1 Objetivo geral
   4.2 Objetivos específicos
5. REFERENCIAL TEÓRICO (ou Fundamentação Teórica)
6. HIPÓTESES (se aplicável)
7. METODOLOGIA
   7.1 Tipo de pesquisa
   7.2 Universo / amostra / sujeitos
   7.3 Procedimentos de coleta
   7.4 Procedimentos de análise
   7.5 Aspectos éticos
8. RESULTADOS ESPERADOS
9. CRONOGRAMA
10. ORÇAMENTO (se aplicável)
11. REFERÊNCIAS (NBR 6023)
12. APÊNDICES / ANEXOS
```

---

## 🎯 Modelo preenchido

```markdown
# PROJETO DE PESQUISA

**Título**: [Título completo, claro, específico — até 15 palavras]

**Subtítulo**: [se houver]

---

## IDENTIFICAÇÃO

| Campo | Conteúdo |
|---|---|
| Pesquisador responsável | Nome Completo Sobrenome |
| Instituição | Universidade Federal do Amazonas — UFAM |
| Programa de Pós-Graduação | PPG em [Nome do Programa] |
| Linha de Pesquisa | [Linha] |
| Orientador | Prof. Dr. Nome do Orientador |
| Coorientador | [se houver] |
| Lattes | http://lattes.cnpq.br/[id] |
| ORCID | 0000-0000-0000-0000 |
| E-mail | autor@dominio.br |
| Edital | [Universal CNPq 2024 / FAPESP 2024 / etc] |
| Modalidade | [Bolsa de Mestrado / Doutorado / PQ / PIBIC] |
| Duração | [12 / 24 / 48 meses] |
| Data | DD de mês de 2026 |

---

## RESUMO

A presente proposta investiga [tema/problema] no contexto de [recorte], adotando [tipo de pesquisa] como abordagem metodológica. Justifica-se pela [relevância acadêmica + relevância social/prática]. Tem como objetivo geral [objetivo]. Como objetivos específicos: a) [obj1]; b) [obj2]; c) [obj3]. Espera-se contribuir com [contribuição teórica + contribuição prática], aportando avanços para [área CAPES]. A pesquisa será desenvolvida em [duração] meses, com cronograma estruturado em [N] etapas, conforme detalhado.

**Palavras-chave**: termo 1; termo 2; termo 3; termo 4; termo 5.

---

## 1 INTRODUÇÃO

### 1.1 Apresentação do tema

[Parágrafo 1] [Apresenta o tema em sua amplitude. 2-3 frases situando o leitor].

[Parágrafo 2] [Cita 2-3 estudos recentes mostrando que o tema é relevante e pertinente].

### 1.2 Problema de pesquisa

[Parágrafo 1] [Recorta o tema até chegar no problema específico que vai investigar].

[Parágrafo 2] [Apresenta a lacuna: o que **não foi feito** ou **mal feito** na literatura].

[Parágrafo 3] [Formula a pergunta de pesquisa de forma direta]:

> **Problema de pesquisa**: [Pergunta clara, específica e respondível]?

### 1.3 Justificativa

[Parágrafo 1 — Justificativa acadêmica] [Por que vale a pena pesquisar? Em que avança a literatura? Que conceitos vai aclarar/revisar?]

[Parágrafo 2 — Justificativa prática/social] [Que problema real isso resolve? Quem se beneficia? Que política, instituição, comunidade pode usar os resultados?]

[Parágrafo 3 — Justificativa institucional] [Por que esse PPG / pesquisador é apropriado pra fazer? Que recursos a instituição oferece?]

---

## 2 OBJETIVOS

### 2.1 Objetivo geral

[Iniciar com verbo no infinitivo: analisar, investigar, mapear, propor, avaliar, descrever, comparar, validar].

> Analisar [...] no contexto de [...].

### 2.2 Objetivos específicos

a) [Verbo + objeto + condição];
b) [Verbo + objeto + condição];
c) [Verbo + objeto + condição];
d) [Verbo + objeto + condição].

⚠️ **Cada objetivo específico deve corresponder a uma fase da metodologia ou um capítulo dos resultados**.

---

## 3 REFERENCIAL TEÓRICO

### 3.1 [Conceito-chave 1]

[Discussão do conceito ancorada em autor canônico]. Como observa Autor (ano, p. X), "[citação direta curta]". A literatura brasileira tem se dedicado a [...] (REFERÊNCIA 1; REFERÊNCIA 2).

### 3.2 [Conceito-chave 2]

[Conecta com o anterior].

### 3.3 Estado da arte

[Mapeia trabalhos relacionados nos últimos 5-10 anos. Mostra a lacuna que o projeto preenche].

---

## 4 HIPÓTESES

(Se a pesquisa for explanatória ou quantitativa)

> **H1**: [Afirmação testável].
> **H2**: [Afirmação testável].
> **H3**: [Afirmação testável].

---

## 5 METODOLOGIA

### 5.1 Tipo de pesquisa

A pesquisa caracteriza-se como [exploratória / descritiva / explicativa] de natureza [básica / aplicada], com abordagem [qualitativa / quantitativa / mista], conforme classificação proposta por Gil (2017). Quanto aos procedimentos técnicos, consiste em [bibliográfica / documental / experimental / estudo de caso / pesquisa-ação / etnográfica / survey].

### 5.2 Universo e amostra (sujeitos da pesquisa)

[Descrição da população:
- Para pesquisa com humanos: critério de inclusão/exclusão, amostragem, tamanho amostral
- Para pesquisa documental: corpus a ser analisado
- Para pesquisa experimental: condições experimentais]

### 5.3 Procedimentos de coleta de dados

[Detalhar instrumentos:
- Questionário (Likert? Aberto? Validado?)
- Entrevista (estruturada/semi/não estruturada)
- Observação (participante/não participante)
- Análise documental
- Coleta computacional (web scraping, APIs)
- Procedimento experimental detalhado]

### 5.4 Procedimentos de análise dos dados

[Detalhar método de análise:
- Análise de Conteúdo (BARDIN, 2011)
- Análise estatística descritiva/inferencial (ferramenta: R, SPSS, JASP)
- Análise de discurso (FAIRCLOUGH, 2008; ORLANDI, 2007)
- Análise por software qualitativo (NVivo, ATLAS.ti, MaxQDA)]

### 5.5 Aspectos éticos

[Se envolver seres humanos:]
O projeto será submetido ao Comitê de Ética em Pesquisa da [Instituição] em conformidade com a Resolução nº 466/2012 do CNS. Será obtido Termo de Consentimento Livre e Esclarecido (TCLE) de todos os participantes. [Etc].

[Se envolver dados sensíveis:]
A coleta e tratamento de dados respeitarão a Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018), com anonimização e armazenamento seguro.

---

## 6 RESULTADOS ESPERADOS

### 6.1 Contribuições teóricas

[Que conceitos serão aprofundados? Que articulações teóricas serão propostas?]

### 6.2 Contribuições práticas

[Que aplicações concretas? Política, sistema, ferramenta, modelo, framework?]

### 6.3 Produção esperada

- **1 dissertação/tese** defendida em [data]
- **2 artigos** em revistas Qualis A1-A3 da área
- **1 trabalho** em evento [SBC/ANPEd/etc]
- **1 capítulo de livro** (se aplicável)
- [Outros: software, patente, política pública]

---

## 7 CRONOGRAMA

### Para pesquisa de 24 meses (Mestrado)

| Atividade | Mês |
|---|---|
| | 1-3 | 4-6 | 7-9 | 10-12 | 13-15 | 16-18 | 19-21 | 22-24 |
|---|---|---|---|---|---|---|---|---|
| Revisão de literatura | ✅ | ✅ | ✅ | ✅ | | | | |
| Submissão ao CEP | ✅ | | | | | | | |
| Coleta de dados | | ✅ | ✅ | ✅ | ✅ | | | |
| Análise dos dados | | | | ✅ | ✅ | ✅ | | |
| Redação da dissertação | | | | | ✅ | ✅ | ✅ | ✅ |
| Submissão de artigos | | | | | | ✅ | ✅ | ✅ |
| Defesa | | | | | | | | ✅ |

### Para pesquisa de 48 meses (Doutorado)
Expandir cronograma proporcionalmente.

---

## 8 ORÇAMENTO

### Para projetos com bolsa + custeio

| Item | Quantidade | Valor unitário | Valor total |
|---|---|---|---|
| Bolsa de Mestrado (24 meses) | 24 | R$ 2.100,00 | R$ 50.400,00 |
| Material bibliográfico | 1 | R$ 1.500,00 | R$ 1.500,00 |
| Software estatístico | 1 | R$ 800,00 | R$ 800,00 |
| Diárias para coleta | 10 | R$ 250,00 | R$ 2.500,00 |
| Passagens | 4 | R$ 800,00 | R$ 3.200,00 |
| Tradução de artigo | 2 | R$ 1.500,00 | R$ 3.000,00 |
| **TOTAL** | | | **R$ 61.400,00** |

⚠️ Verifique valores atualizados de cada agência. CNPq tem tabela própria.

---

## 9 REFERÊNCIAS

[Lista alfabética conforme NBR 6023:2018]

BARDIN, Laurence. **Análise de conteúdo**. São Paulo: Edições 70, 2011.

GIL, Antonio Carlos. **Como elaborar projetos de pesquisa**. 6. ed. São Paulo: Atlas, 2017.

[outras]

---

## 10 APÊNDICES (opcional)

- **Apêndice A** — Roteiro de entrevista
- **Apêndice B** — Modelo de TCLE
- **Apêndice C** — Termo de uso de imagem (se aplicável)

## 11 ANEXOS (opcional)

- **Anexo A** — Comprovante de aprovação do CEP (quando obtido)
- **Anexo B** — [Outros]
```

---

## 🎯 Dicas específicas por edital

### CNPq Universal
- Limite de palavras: 1.000 no resumo, máximo 30 páginas total
- Justificativa **acadêmica + impacto social** valem muito
- **Inclua infraestrutura** disponível (laboratórios, equipamentos)
- Mencione **interação com outros grupos** se houver

### FAPESP / FAPs estaduais
- Foco em **regional** (estado da agência)
- **Prazo de pagamento de bolsa** geralmente trimestral
- Custeio mais flexível

### Edital de Bolsa CAPES (PROEX, PRINT)
- **Internacionalização** é palavra-chave
- Inclua **parceria internacional** (institucional/individual)
- Mencione **publicação em revista internacional**

### Edital PIBIC (graduação)
- Mais simples e curto (10-15 páginas)
- Foco em **iniciação científica**: aprendizado do método
- Não exige resultados originais como mestrado/doutorado

---

## 🚨 Erros que reprovam projeto

❌ Sem pergunta de pesquisa explícita
❌ Objetivos genéricos ("aprender sobre [tema]")
❌ Justificativa só "porque é importante" sem por quê
❌ Metodologia genérica ("pesquisa qualitativa")
❌ Cronograma irrealista (mestrado em 6 meses)
❌ Orçamento sem detalhamento
❌ Referências bibliográficas só de Wikipedia / Google
❌ Sem ancoragem em autor canônico
❌ Sem mostrar a lacuna na literatura
❌ Sem mencionar aspectos éticos quando envolve humanos
❌ Citar revista predatória ou Qualis C
❌ Erros de português

---

## ✅ Checklist final

- [ ] Identificação completa (Lattes, ORCID, instituição)
- [ ] Resumo dentro do limite de palavras
- [ ] Pergunta de pesquisa clara
- [ ] Objetivo geral + 3-5 específicos com verbos no infinitivo
- [ ] Justificativa em 3 dimensões (acadêmica, prática, institucional)
- [ ] Referencial cita pelo menos 1 autor canônico do tema
- [ ] Metodologia replicável
- [ ] Cronograma realista com Gantt
- [ ] Orçamento detalhado (se aplicável)
- [ ] Aspectos éticos mencionados
- [ ] Referências NBR 6023 (mín 20-30)
- [ ] Apêndices (instrumentos de coleta) anexados
