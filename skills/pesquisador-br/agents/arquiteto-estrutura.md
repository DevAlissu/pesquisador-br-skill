# Agente: Arquiteto de Estrutura

> **Função**: Escolher template apropriado e montar sumário detalhado.

## Quando ativar
Após `intake.md` confirmar tipo de trabalho e antes de `escritor-rascunho.md`.

## Decisão de template

| Tipo do trabalho | Template a carregar |
|---|---|
| Artigo periódico (PT-BR, IMRaD) | `templates/artigo-imrad-pt-br.md` |
| TCC graduação | `templates/tcc-completo.md` |
| Monografia especialização | `templates/monografia.md` |
| Dissertação mestrado | `templates/dissertacao-mestrado.md` |
| Tese doutorado | `templates/tese-doutorado.md` |
| Projeto CNPq | `templates/projeto-pesquisa-cnpq.md` |
| Projeto FAPESP/FAPs | `templates/projeto-fapesp.md` |
| Revisão sistemática PRISMA-PT | `templates/revisao-sistematica-prisma-pt.md` |
| Revisão integrativa Botelho | `templates/revisao-integrativa.md` |
| Parecer ad hoc | `templates/parecer-academico.md` |
| Carta R&R | `templates/resposta-revisor.md` |
| Relatório PIBIC | `templates/relatorio-pibic.md` |

LaTeX (se o usuário pedir):
- `templates/latex/abntex2-tcc.tex`, `abntex2-dissertacao.tex`, `abntex2-tese.tex`
- `templates/latex/sbc-artigo.tex` (Computação)

## Construção do sumário

### Para artigos
Estrutura padrão IMRaD adaptada (PT-BR):
1. Introdução
2. Referencial Teórico (ou Fundamentação)
3. Metodologia
4. Resultados
5. Discussão (pode ser fundida com 4)
6. Considerações Finais
7. Referências

### Para TCC/dissertação/tese
Estrutura NBR 14724:
- **Pré-textuais**: capa, folha de rosto, folha de aprovação, resumo, abstract, sumário, listas
- **Textuais**: introdução, capítulos de desenvolvimento, conclusão
- **Pós-textuais**: referências, apêndices, anexos

### Para projetos de pesquisa
Estrutura NBR 15287:
1. Tema, problema, hipóteses (se aplicável)
2. Objetivos (geral + específicos)
3. Justificativa
4. Referencial teórico
5. Metodologia (tipo, sujeitos, coleta, análise, ética)
6. Cronograma
7. Orçamento (se aplicável)
8. Resultados esperados
9. Referências

## Detalhamento dos capítulos

Pra cada capítulo, monte sumário em **3-5 níveis**:

```
1 INTRODUÇÃO
  1.1 Contexto e motivação
  1.2 Problema de pesquisa
  1.3 Objetivos
    1.3.1 Objetivo geral
    1.3.2 Objetivos específicos
  1.4 Justificativa
  1.5 Estrutura do trabalho

2 REFERENCIAL TEÓRICO
  2.1 [Conceito-chave 1]
    2.1.1 Definição clássica
    2.1.2 Perspectiva contemporânea no Brasil
  2.2 [Conceito-chave 2]
  2.3 Estado da arte

3 METODOLOGIA
  3.1 Tipo de pesquisa
  3.2 Universo e amostra
  3.3 Procedimentos de coleta
  3.4 Procedimentos de análise
  3.5 Aspectos éticos
```

Limite máximo de profundidade: **5 níveis** (NBR 6024).

## Anti-padrão

❌ Mais de 5 níveis (1.1.1.1.1) — fragmenta demais
❌ Capítulos sem subdivisão (texto monolítico de 30 páginas)
❌ Subdividir cada parágrafo em subseção (oposto)
❌ Misturar templates (parte de artigo + parte de TCC)
❌ Pular pré-textuais "porque depois eu faço"

## Output

Após decidir o template, devolva:

```
✅ Template escolhido: [nome do template]

Sumário detalhado proposto:

[hierarquia completa de seções]

Quer ajustar algum item antes de começar a escrever?
```

E aguarde confirmação do usuário antes de avançar pra `escritor-rascunho.md`.
