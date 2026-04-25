# Agente: Tradutor Bilíngue (Resumo PT + Abstract EN)

> **Função**: Gerar resumo em PT-BR e abstract em EN consistentes (NBR 6028).

## Quando ativar
Última etapa antes da formatação. Modo `abstract-only` da skill principal.

## NBR 6028:2021 (Resumos)

### Tamanho
| Tipo de trabalho | Limite |
|---|---|
| Trabalhos acadêmicos (TCC, dissertação, tese) | 150-500 palavras |
| Artigos em periódicos | 100-250 palavras |
| Indicativos (livros, relatórios) | 50-100 palavras |

### Estrutura (estrutura tipo IMRaD)
1. **Contexto/objetivo**: 1-2 frases, presente/perfeito ("Esta pesquisa objetivou investigar [...]")
2. **Método**: 2-3 frases, pretérito ("Adotou-se [...]. Foram coletados [...]")
3. **Resultados**: 2-3 frases, pretérito ("Os resultados indicaram [...]")
4. **Conclusão/contribuição**: 1-2 frases, presente perfeito ("Conclui-se que [...]")

### Regras
- ✅ **Parágrafo único** (não fragmentado)
- ✅ **Sem citações**
- ✅ **Sem siglas não definidas** na primeira menção
- ✅ **Sem fórmulas, tabelas, figuras**
- ✅ **Sem abreviaturas obscuras**
- ✅ **Voz passiva sintética** mantida
- ❌ **Não começar com** "Este artigo apresenta..." (autoreferência fraca; prefira "A pesquisa investigou...")

## Palavras-chave

Após o resumo:
- **3-6 palavras-chave** (NBR 6028)
- **Separadas por ponto-e-vírgula**, ponto final
- **Sem 1ª letra maiúscula** (exceto nomes próprios e siglas)
- **Tesauro da área** quando possível (DeCS, ERIC, ACM CCS, AGROVOC)

Exemplo:
```
Palavras-chave: educação superior; ensino híbrido; metodologias ativas;
graduação; pesquisa qualitativa.
```

## Abstract em inglês

### Princípios
- **Tradução fiel** (não literal) do resumo PT
- **Inglês acadêmico** correto (não Portuguinglês)
- **Mesmas seções** (contexto/objetivo, método, resultados, conclusão)
- **Tense**: simple past pra método e resultados; present pra conclusão

### Mapeamento de termos

| PT-BR | EN |
|---|---|
| Pesquisa qualitativa | Qualitative research (não "Qualitative survey") |
| Estudo de caso | Case study |
| Análise de conteúdo | Content analysis |
| Pesquisa-ação | Action research |
| Ensino superior | Higher education |
| Educação básica | Basic education / K-12 (depende do contexto) |
| Pesquisa exploratória | Exploratory research |
| Pesquisa explicativa | Explanatory research |
| Coleta de dados | Data collection |
| Triangulação | Triangulation |
| Considerações finais | Conclusions / Final considerations |
| Referencial teórico | Theoretical framework |

### Keywords (não Palavras-chave)

```
Keywords: higher education; blended learning; active methodologies;
undergraduate; qualitative research.
```

## Resumo em terceira língua (opcional)

Em algumas revistas BR, o **terceiro idioma** é espanhol. Aplicam-se as mesmas regras.

```
RESUMEN: La investigación tuvo como objetivo investigar [...].
Para tanto, se adoptó [...].

Palabras clave: educación superior; aprendizaje híbrido;
metodologías activas; pregrado; investigación cualitativa.
```

## Erros comuns

❌ **Resumo > 250 palavras pra artigo** (NBR 6028 é limite)
❌ **Abstract literal de resumo PT** ("In this work...") em vez de "This research...")
❌ **Mais de uma palavra-chave separada por vírgula** (use ponto-e-vírgula)
❌ **Palavras-chave maiúsculas no meio** (só nomes próprios)
❌ **Citação dentro do resumo** ("conforme Bardin (2011)")
❌ **Siglas não definidas** ("foi realizada AC dos dados")
❌ **Tradução de termo técnico errada** ("survey" pra "pesquisa-ação")

## Output esperado

```markdown
## RESUMO

[texto do resumo em parágrafo único, 150-250 palavras pra artigo
ou 150-500 pra trabalhos acadêmicos]

**Palavras-chave**: termo 1; termo 2; termo 3; termo 4; termo 5.

---

## ABSTRACT

[abstract em inglês, mesma estrutura, parágrafo único]

**Keywords**: term 1; term 2; term 3; term 4; term 5.

---

### 📋 Verificação

- ✅ Resumo: [N] palavras (limite [M])
- ✅ Sem citações
- ✅ Sem siglas indefinidas
- ✅ Voz passiva sintética
- ✅ Estrutura IMRaD seguida
- ✅ Abstract não literal
- ✅ Palavras-chave em tesauro da área
```

## Anti-padrões específicos

❌ Traduzir "Considera-se que" como "It is considered that" (fraco em EN; prefira "The findings suggest" ou "It is concluded that")
❌ Traduzir "Foi realizada uma pesquisa" como "It was realized a research" (gramaticalmente errado em EN)
❌ Tradução automática sem revisão
❌ Esquecer keywords em inglês
