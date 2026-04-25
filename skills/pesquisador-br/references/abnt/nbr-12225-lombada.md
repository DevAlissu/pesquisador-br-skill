# NBR 12225:2004 — Lombada

> Estabelece a apresentação da **lombada** (parte lateral) de livros, teses, dissertações e outros trabalhos acadêmicos.

## Definição

**Lombada**: parte da capa que une as folhas, geralmente com **3-15 mm de espessura** dependendo do número de páginas. É o que aparece na estante.

⚠️ A lombada **só existe** em obras encadernadas em **espiral, brochura ou capa dura**. Em encadernação simples (grampos, espiral fina), pode não haver espaço para texto na lombada.

---

## Elementos obrigatórios na lombada

### 1. Nome do(a) autor(a)
- Sobrenome em **MAIÚSCULAS**
- Nome próprio em maiúsculas e minúsculas
- Pode ser abreviado: "SILVA, J. A." ou completo "SILVA, José Alberto"

### 2. Título do trabalho
- Em **MAIÚSCULAS** ou em capitalização normal
- Pode ser **abreviado** se a lombada for fina (>4 cm a partir do topo)
- Subtítulo geralmente é omitido (espaço)

### 3. Elementos alfanuméricos de identificação
- **Ano** de publicação ou defesa
- Pode incluir **volume** ou **tomo**, se houver

### Exemplo de elementos
```
SILVA, J. A.   ANÁLISE DA EDUCAÇÃO INCLUSIVA   2026
```

---

## Sentido da escrita

A NBR 12225 admite **dois sentidos**:

### Sentido descendente (mais comum no Brasil)
Lê-se de **cima pra baixo**:

```
┌─┐
│S│
│I│
│L│
│V│
│A│
└─┘
```

### Sentido horizontal (lombada larga)
Quando a lombada tem espessura suficiente (geralmente >40 mm):

```
┌──────────────┐
│  SILVA, J.   │
│  ANÁLISE...  │
│      2026    │
└──────────────┘
```

⚠️ A norma brasileira é descendente. **Padrão internacional** (livros estrangeiros) é ascendente. Se for trabalho acadêmico BR, **use descendente**.

---

## Logos / símbolos da instituição

✅ Pode incluir, geralmente no **rodapé** da lombada:
- Logo da IES
- Logo da editora
- Logo do PPG

⚠️ Se for tese/dissertação, geralmente leva **logo da IES** + sigla:
```
SILVA, J. A. | ANÁLISE... | 2026 | UEA
```

---

## Tipografia

- **Fonte**: mesma da capa (Times New Roman, Arial)
- **Tamanho**: legível à distância (geralmente **14-18 pt**)
- **Cor**: preto sobre fundo claro / branco sobre fundo escuro
- **Negrito**: opcional, mas recomendado para sobrenome e título

---

## Exemplo completo (TCC)

```
┌─────────────────────────┐
│         (topo)          │
│                         │
│      SILVA, J. A.       │  ← Autor (negrito)
│                         │
│  ESTRATÉGIAS PEDAGÓGICAS│  ← Título (pode abreviar)
│  PARA EDUCAÇÃO INCLUSIVA│
│                         │
│         (...)           │
│                         │
│         2026            │  ← Ano
│                         │
│         UEA             │  ← Sigla IES (opcional)
│       (rodapé)          │
└─────────────────────────┘
```

---

## Exemplo de tese (encadernação capa dura)

```
SILVA, J. A.
A FORMAÇÃO DOCENTE NO ENSINO REMOTO:
DESAFIOS E PERSPECTIVAS NO PÓS-PANDEMIA
2026
[logo UFRGS]
```

---

## Como gerar (Word / LaTeX)

### Word
- Configure tamanho da página: largura = espessura da lombada, altura = altura do livro
- Use Tabela invisível com 3 linhas (autor, título, ano)
- Texto **vertical** (sentido descendente): rotacionar -90°

### LaTeX (abnTeX2)
Não há comando nativo padrão. Soluções:
- Pacote `pgf` ou `tikz` para texto rotacionado
- Pacote `geometry` para configurar página da lombada
- Compilação separada da lombada como página única

⚠️ Lombada **geralmente é gerada pela gráfica** que faz a impressão final. O autor entrega o PDF e a gráfica monta com base nas medidas.

---

## Encadernação que tem ou não tem lombada

| Tipo | Tem lombada? |
|---|---|
| **Brochura** (cola lateral) | Sim, geralmente |
| **Capa dura** | Sim, sempre |
| **Espiral fina** | Não |
| **Espiral grossa** | Sim, mas estreita |
| **Grampo** | Não |
| **Wire-O** | Sim, estreita |

Pra TCC, **a maioria das IES exige brochura**, com lombada.

---

## Erros frequentes

❌ **Lombada vazia** (esqueceu de configurar)
❌ **Sentido errado** (ascendente em vez de descendente)
❌ **Autor por extenso** quando lombada é fina (cabe sobrenome só)
❌ **Sem ano**
❌ **Subtítulo extenso** que não cabe (omita ou abrevie)
❌ **Fonte muito pequena** (< 10 pt fica ilegível)
❌ **Cor que não contrasta** (azul claro sobre branco, p.ex.)

---

## Boas práticas

✅ **Coordene com a gráfica** que vai imprimir (ela conhece as medidas)
✅ **Imprima protótipo** antes de tirar a tiragem final
✅ **Confira o sentido** descendente (BR) ou ascendente (internacional)
✅ **Use mesma fonte** da capa para consistência
✅ **Inclua ano** (norma exige)
✅ **Logo institucional opcional** mas elegante

---

## Fonte oficial

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 12225**: informação e documentação — lombada — apresentação. Rio de Janeiro: ABNT, 2004.

---

## Recursos

- Manual de TCC da sua IES (geralmente especifica fonte/tamanho da lombada)
- Gráfica que faz a impressão (ela tem as medidas exatas)
- Ver `nbr-14724-trabalhos.md` para capa e folha de rosto
