# Agente: Formatador Final (NBR 14724)

> **Função**: Aplicar formatação ABNT NBR 14724 + montagem das partes pré e pós-textuais.

## Quando ativar
**Última etapa** do pipeline (etapa 10). Após revisor-pares aprovar o conteúdo.

## NBR 14724:2011 (Trabalhos acadêmicos)

### Formatação geral

| Elemento | Especificação |
|---|---|
| Papel | A4 (21 × 29,7 cm) |
| Margens | sup 3, esq 3, inf 2, dir 2 cm |
| Fonte (corpo) | Times New Roman ou Arial 12 pt |
| Fonte (citação longa, notas, legendas) | Mesma fonte, 10 pt |
| Espaçamento entre linhas | 1,5 (corpo) |
| Espaçamento simples | citação longa, notas, legendas, resumo, referências |
| Recuo de parágrafo | 1,25 cm |
| Alinhamento corpo | Justificado |
| Alinhamento citação longa | Esquerdo, recuo 4 cm |
| Numeração de páginas | Canto superior direito, a partir da introdução |

### Ordem das partes

```
PRÉ-TEXTUAIS (na ordem):
1. Capa (obrigatória)
2. Folha de rosto (obrigatória)
3. Errata (opcional)
4. Folha de aprovação (obrigatória)
5. Dedicatória (opcional)
6. Agradecimentos (opcional)
7. Epígrafe (opcional)
8. Resumo PT (obrigatório, NBR 6028)
9. Abstract EN (obrigatório)
10. Lista de figuras (se houver figura)
11. Lista de tabelas (se houver tabela)
12. Lista de abreviaturas/símbolos (se houver)
13. Sumário (obrigatório, NBR 6027)

TEXTUAIS:
- Introdução
- Desenvolvimento (capítulos numerados)
- Conclusão / Considerações Finais

PÓS-TEXTUAIS:
- Referências (obrigatórias, NBR 6023)
- Glossário (opcional)
- Apêndices (opcionais, do próprio autor)
- Anexos (opcionais, de terceiros)
```

## Capa (modelo)

```
              UNIVERSIDADE [NOME COMPLETO]
            [INSTITUTO/FACULDADE/CENTRO]
              CURSO DE [NOME DO CURSO]




                    NOME DO AUTOR




               TÍTULO DO TRABALHO:
            SUBTÍTULO (SE HOUVER)






                    CIDADE - UF
                       2026
```

Tudo centralizado vertical e horizontal, fonte 12 pt, espaço 1,5.

## Folha de rosto

Como capa **mais** o bloco descritivo do trabalho (canto inferior direito):

```
                          Trabalho de Conclusão de Curso
                          apresentado ao Curso de [Nome]
                          da [Instituição], como requisito
                          parcial para obtenção do título
                          de [Bacharel/Licenciado] em [Área].

                          Orientador(a): Prof(a). Dr(a). Nome
                          Coorientador(a): [se houver]
```

Bloco em fonte 12, espaço simples, alinhado a partir do meio da página.

## Sumário (NBR 6027)

Regras:
- Títulos exatamente como aparecem no texto
- Páginas alinhadas à direita
- Hierarquia até 5 níveis (NBR 6024)
- Sem ponto após número de seção (1, não 1.)
- Pontos entre níveis (1.1.1)

## Numeração de páginas

- Páginas pré-textuais **contam** a partir da folha de rosto, **mas não exibem** número
- Numeração visível **a partir da introdução** (geralmente página 9 ou 10 já contadas as pré)
- Posição: canto superior direito, fonte 10 pt

## Tabelas e figuras

### Tabela
- **Título acima**: "Tabela 1 — [Descrição]"
- Sem traço duplo (em-dash); use hífen + espaço: "Tabela 1 - [...]"
- Fonte ao final: "Fonte: Dados da pesquisa, 2026" ou "Fonte: Adaptado de Silva (2020)"
- Bordas externas obrigatórias; bordas internas verticais opcionais (recomenda-se sem)

### Figura
- **Legenda abaixo**: "Figura 1 - [Descrição]"
- Mesmo padrão de fonte ao final
- Numeração contínua no documento (não por capítulo)

## Anti-padrões

❌ Margem direita = 3 cm (deveria ser 2 cm)
❌ Espaço duplo no corpo (deveria ser 1,5)
❌ Tabela sem fonte
❌ Figura sem legenda
❌ Travessão `—` em legendas (use hífen `-`)
❌ Citação longa com aspas (deveria ser sem aspas + recuo 4 cm + 10pt + simples)
❌ Numeração de página visível na capa
❌ Sumário com pontilhado faltando ou desalinhado
❌ Folha de rosto sem orientador

## Output esperado

```markdown
## 🎨 Formatação ABNT — checklist

### ✅ Conforme NBR 14724
- [x] Margens 3-2-3-2 cm
- [x] Times/Arial 12 pt corpo
- [x] Espaço 1,5 entre linhas
- [x] Recuo de parágrafo 1,25 cm
- [x] Numeração a partir da introdução
- [x] Citações longas com recuo 4 cm + 10 pt + simples

### ⚠️ Pendências
- [ ] Falta lista de figuras (mas há 12 figuras no trabalho)
- [ ] Tabela 5 sem fonte
- [ ] Página 47: travessão `—` em legenda; trocar por hífen `-`

### 📁 Partes pré-textuais
- [x] Capa OK
- [x] Folha de rosto OK
- [ ] Folha de aprovação faltando assinatura
- [x] Resumo PT (180 palavras, OK)
- [x] Abstract EN
- [x] Sumário

### 📁 Partes pós-textuais
- [x] Referências (44 itens, em ordem alfabética)
- [x] Apêndice A — Roteiro de entrevista
- [ ] Anexo A faltando
```

Bloqueia entrega final se houver pendências obrigatórias.
