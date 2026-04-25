# NBR 6027:2012 — Sumário

> Estabelece a apresentação do sumário em trabalhos acadêmicos brasileiros.

## Definição

**Sumário**: enumeração das principais divisões, seções e demais partes de um trabalho, na mesma ordem e grafia em que se apresentam no texto, **acompanhado dos respectivos números das páginas**.

## Localização

- Aparece **após as listas** (de figuras, tabelas, abreviaturas)
- **Antes** da introdução
- Início em página própria, ímpar (em frente e verso)

## Estrutura básica

```
                          SUMÁRIO

1 INTRODUÇÃO ............................................. 9

2 REFERENCIAL TEÓRICO ................................... 12
2.1 [SUBSEÇÃO] .......................................... 12
2.2 [SUBSEÇÃO] .......................................... 18

3 METODOLOGIA ........................................... 22
3.1 Tipo e abordagem da pesquisa ........................ 22
3.2 Sujeitos / corpus ................................... 24
3.3 Procedimentos de coleta ............................. 25
3.4 Procedimentos de análise ............................ 26

4 RESULTADOS E DISCUSSÃO ................................ 27
4.1 [...]
4.2 [...]

5 CONSIDERAÇÕES FINAIS .................................. 45

REFERÊNCIAS ............................................. 48
APÊNDICE A — [TÍTULO] .................................. 53
ANEXO A — [TÍTULO] ..................................... 56
```

## Regras

### 1. Títulos exatamente como no texto
✅ Se no texto está `1.1 Contextualização do problema`, no sumário também
❌ Não pode ser abreviado nem reformulado

### 2. Hierarquia tipográfica idêntica ao texto
- Seção primária (1, 2, 3): MAIÚSCULAS, NEGRITO, 12 pt
- Seção secundária (1.1, 2.1): Maiúsculas iniciais, NEGRITO, 12 pt
- Terciária (1.1.1): Maiúsculas iniciais, sem negrito, 12 pt
- Quaternária e quinária: minúsculas, sem destaque

### 3. Pontilhado conectando título e página
✅ Conexão por **pontos** ou linha conectora:
```
1.2 Problema de pesquisa ............................ 12
```

❌ Sem conexão, com espaço grande:
```
1.2 Problema de pesquisa                                12
```

### 4. Páginas alinhadas à direita
- Números de página alinhados em coluna à direita
- Mesma fonte e tamanho do texto

### 5. Espaçamento
- Entre itens: espaço **simples** ou **1,5** (manter consistência)
- Recuo conforme nível: `1`, `  1.1`, `    1.1.1`

### 6. Apêndices e anexos
- **Sem número de capítulo** (não continua a numeração do texto)
- Letra maiúscula: `APÊNDICE A`, `APÊNDICE B`, `ANEXO A`
- Travessão hífen entre indicação e título: `APÊNDICE A — [Título]`

⚠️ **Note**: nem todos os trabalhos têm apêndice/anexo. Listar só o que existe.

### 7. Glossário (se houver)
Apresentado **antes das referências** no sumário:
```
GLOSSÁRIO ............................................... 47
REFERÊNCIAS ............................................. 50
```

## Tipos de sumário

### Sumário tradicional (mais comum)
- Títulos sem destaque pra capa de capítulo
- Mostra todos os níveis (até 5)

```
SUMÁRIO

1 INTRODUÇÃO ............................................. 9
1.1 Contextualização ................................... 10
1.2 Problema ........................................... 12

2 REFERENCIAL ........................................... 16
```

### Sumário capitulado (alternativa)
- Capítulos separados visualmente

```
SUMÁRIO

CAPÍTULO 1 — INTRODUÇÃO
1.1 Contextualização ................................... 10
1.2 Problema ........................................... 12

CAPÍTULO 2 — REFERENCIAL TEÓRICO
2.1 ...
```

⚠️ A NBR 6027 admite mas não recomenda explicitamente. Use o tradicional.

## Geração automática

### Word
- Use **Estilos** (Título 1, Título 2, Título 3) consistentemente
- Inserir → Sumário → Sumário automático
- Atualizar antes de imprimir

### LaTeX (abnTeX2)
- Use `\chapter{}`, `\section{}`, `\subsection{}` etc
- `\tableofcontents` ou `\tableofcontents*` (sem * = inclui no próprio sumário)

### Google Docs
- Estilos pré-definidos
- Inserir → Índice → Com números de página

## Erros frequentes

❌ **Sumário não bate com texto**: títulos diferentes, página errada
   → Sempre regenere depois de mudar texto

❌ **Sem pontilhado**: difícil de ler

❌ **Páginas desalinhadas**: visualmente desorganizado

❌ **Apêndices com número de capítulo**: errado, deve ser só letra
   - Errado: `6 APÊNDICE A`
   - Certo: `APÊNDICE A — [Título]`

❌ **Sumário vazio em capítulo**: `2 REFERENCIAL TEÓRICO` sem subseções listadas
   → Liste as subseções importantes

❌ **Hierarquia tipográfica inconsistente**: alguns títulos em negrito, outros não
   → Mantenha o padrão por nível

❌ **Numeração faltando**: pular de 2.1 para 2.3 sem 2.2

## Boas práticas

✅ **Use estilos** no editor (Word, LibreOffice, LaTeX)
✅ **Atualize automaticamente** antes de imprimir/exportar
✅ **Confira** os números de página manualmente após exportar PDF
✅ **Inclua glossário** se o trabalho usa termos técnicos
✅ **Mantenha** consistência tipográfica com o texto
✅ **Liste apêndices e anexos** com seus títulos completos

## Sumário curto vs longo

### Para artigos
- Geralmente **não tem** sumário (texto curto)
- Cabeçalhos numerados servem de orientação

### Para TCC
- Sumário **simples**, 1-2 páginas
- Inclui pré-textuais opcionais (lista de figuras, etc) e pós-textuais

### Para dissertação/tese
- Sumário **detalhado**, pode ocupar 3-5 páginas
- Inclui todos os níveis até quaternário (1.1.1.1)

## Fonte oficial

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6027**: informação e documentação — sumário — apresentação. Rio de Janeiro: ABNT, 2012.
