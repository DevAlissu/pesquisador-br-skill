# NBR 6034:2004 — Índice

> Estabelece a apresentação de **índice** (ou "índice remissivo") em livros, teses, dissertações e documentos técnicos.

## Definição

**Índice**: lista de palavras ou frases ordenadas, indicando informações específicas no texto **com remissão de página**.

⚠️ **Não confunda** com **sumário** (NBR 6027). Diferenças:

| Aspecto | Sumário | Índice |
|---|---|---|
| **O que mostra** | Estrutura do trabalho | Conceitos / nomes específicos |
| **Ordenação** | Sequencial (capítulo 1, 2, 3) | Alfabética |
| **Localização** | Início (após pré-textuais) | **Final** (após referências/anexos) |
| **Obrigatório** | Sim, sempre | **Não** (opcional) |

---

## Quando usar índice

✅ **Útil em**:
- Livros didáticos / técnicos
- Manuais
- Teses e dissertações **longas** (>200 páginas)
- Trabalhos com muitos conceitos / nomes próprios

❌ **Geralmente não tem**:
- TCC (curto demais)
- Artigo (não cabe)
- Dissertação simples
- Trabalhos curtos

---

## Tipos de índice

### 1. Índice de assuntos (mais comum)
Conceitos, temas, palavras-chave organizadas alfabeticamente.

```
ÍNDICE

A
abordagem qualitativa, 45-48, 67
análise de conteúdo
   Bardin, 78-82
   pré-análise, 80
   exploração do material, 81
ANPEd, 12, 145

B
Bardin, Laurence, 78-82, 90, 124
BDTD, 33, 59, 102

C
CAPES, 14, 16, 28-30
   Documento de Área, 28
   Qualis, 29
   Sucupira, 30
```

### 2. Índice de autores (em obras com muitos autores)
Lista de autores citados no texto com páginas.

```
ÍNDICE ONOMÁSTICO

BARDIN, L., 78-82, 90, 124
BAUER, M. W., 67
GIL, A. C., 45, 100, 115
MINAYO, M. C. S., 39, 67, 89, 124
SILVA, J. A., 156
```

### 3. Índice de tabelas e figuras
Algumas IES exigem listas separadas (que ficam **antes** do sumário, nos pré-textuais — não confunda).

### 4. Índice cruzado
Cruzamento de assuntos com remissões "ver também":
```
educação inclusiva, 89-95
   ver também: deficiência, NEE, atendimento educacional especializado
```

---

## Como gerar (Word)

### Marcar entradas
1. Selecione termo no texto
2. Menu **Referências** → **Marcar entrada de índice**
3. Confirme entrada principal e subentradas
4. Repita pra cada termo importante

### Inserir índice
1. Posicione cursor no final do trabalho (após referências, anexos)
2. Menu **Referências** → **Inserir índice**
3. Escolha formato (1 ou 2 colunas, com pontilhado, etc)
4. Atualize após mudanças no texto

### Atualização
- Sempre que **alterar texto**, atualize o índice (botão direito → "atualizar campo")
- Antes de imprimir/exportar PDF, atualize **uma última vez**

---

## Como gerar (LaTeX)

```latex
\usepackage{makeidx}
\makeindex

\begin{document}
% No corpo do texto:
A análise de conteúdo \index{análise de conteúdo} é proposta
por Bardin \index{Bardin, Laurence}.

% No final:
\printindex
\end{document}
```

Compile com:
```bash
pdflatex doc
makeindex doc
pdflatex doc
```

---

## Regras de ordenação

### Alfabética rigorosa
- "Análise" antes de "ANPEd" antes de "Aprendizagem"
- Acentos **não** alteram ordem ("São Paulo" entre "santidade" e "saúde")
- Maiúsculas e minúsculas são iguais para ordem

### Subentradas
Indentadas, em ordem alfabética:
```
análise de conteúdo
   Bardin, 78-82
   exploração do material, 81
   pré-análise, 80
   tratamento dos resultados, 82
```

### Números no início
Convertem-se em palavras:
- "5 padrões" → ordenado em "C" (cinco)

### Nomes compostos
"São Paulo" — ordenado em "S"

---

## Tipografia

- **Mesma fonte** do texto (Times/Arial 12 pt)
- **Espaçamento simples** entre entradas
- **Espaçamento duplo** entre letras (A, B, C... como divisores)
- **Letras divisoras** podem ser destacadas (negrito, maiúsculas)
- **Páginas em algarismos arábicos** (12, não doze)
- **Intervalo**: hífen sem espaço (45-48, não 45 - 48)
- **Lista**: vírgula entre páginas isoladas (12, 18, 25)

---

## Exemplo completo

```
ÍNDICE

A
abordagem
   mista, 67-70
   qualitativa, 45-48, 67
   quantitativa, 50-55
amostra
   intencional, 69
   por conveniência, 68
análise de conteúdo, 78-82
ANPEd, 12, 145

B
Bardin, Laurence, 78-82, 90, 124
BDTD, 33, 59, 102

C
CAPES
   Documento de Área, 28
   Qualis, 29-31
   Sucupira, 30
CEP, 102-105

[...]
```

---

## Erros frequentes

❌ **Não atualizar** o índice após mudanças no texto (páginas erradas)
❌ Confundir com **sumário**
❌ Posicionar **antes** das referências (deve ser depois)
❌ Página de cada entrada **errada** (Word não atualizou)
❌ **Ordem alfabética errada** (importação manual sem ordenar)
❌ **Subentradas sem indentação**
❌ **Múltiplas entradas pra mesmo conceito** ("A. C.", "Análise de Conteúdo", "AC")
❌ Esquecer **intervalo** de páginas (45-48, não só 45)

---

## Boas práticas

✅ **Marque enquanto escreve**, não no fim
✅ **Use entradas consistentes** (escolha "Análise de Conteúdo" e mantenha)
✅ **Inclua sinônimos** com remissão "ver"
✅ **Atualize antes de exportar PDF**
✅ **Confira manualmente** uma amostra de páginas

---

## Quando criar 2+ índices

### Em teses longas, pode ter:
1. **Índice onomástico** (autores)
2. **Índice de assuntos** (conceitos)
3. **Índice geográfico** (lugares — útil em História, Geografia)
4. **Índice de tabelas** (na verdade vai antes, com listas)

⚠️ Cada índice em página própria, com cabeçalho identificando.

---

## Fonte oficial

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6034**: informação e documentação — índice — apresentação. Rio de Janeiro: ABNT, 2004.

---

## Recursos

- Tutorial Word: Inserir índice automatizado
- Pacote LaTeX `makeidx` (built-in)
- Ver `nbr-6027-sumario.md` para diferença entre sumário e índice
- Ver `nbr-14724-trabalhos.md` para estrutura geral
