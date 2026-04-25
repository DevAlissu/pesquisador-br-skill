# Como Consultar o Qualis CAPES (Sucupira)

> Passo a passo pra descobrir o estrato de uma revista.

## Passo a passo

### 1. Acesse a Plataforma Sucupira

URL: https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf

(Bookmark esse link — é o oficial.)

### 2. Selecione "Evento de Classificação"

⚠️ **Vigente**: "Classificações de Periódicos Quadriênio 2017-2020"

Quando o quadriênio 2021-2024 for liberado, selecione o mais recente.

### 3. Selecione "Área de Avaliação"

Selecione a **área CAPES da sua pesquisa** (ver `areas-capes.md` para a lista das 49 áreas).

⚠️ Importante: a mesma revista pode ter Qualis diferente em áreas diferentes. Sempre filtre pela área CERTA do seu trabalho.

### 4. Filtre por título OU ISSN

**ISSN é mais preciso** (ex: `1678-4456`):
- Toda revista científica tem ISSN (impresso e/ou online)
- Achar ISSN: site da revista, página de submissão, ou Google "[nome revista] ISSN"

**Título** funciona com busca parcial:
- "Cadernos de Pesquisa" retorna várias
- Marque a área certa pra refinar

### 5. Clique "Consultar"

Resultado mostra:
- Nome do periódico
- ISSN
- **Estrato** (A1, A2, A3, A4, B1, B2, B3, B4, C)
- Área de avaliação correspondente

### 6. Anote o estrato

Salve numa planilha:

| Revista | ISSN | Área | Qualis | Tempo médio (peer review) | OA / pago |
|---|---|---|---|---|---|
| Cadernos de Pesquisa | 0100-1574 | Educação | A1 | 90 dias | OA |
| ... | | | | | |

---

## Atalho via URL com filtros

Substitua `[CODIGO_AREA]` pelo código da área (ver `areas-capes.md`):

```
https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf?eventoIni=001&areaCodigo=[CODIGO_AREA]
```

Exemplo (Educação, código `70800006`):
```
https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf?eventoIni=001&areaCodigo=70800006
```

---

## Buscas em lote (várias revistas de uma vez)

⚠️ A Sucupira **não permite busca em lote oficial** (sem API pública).

Alternativas:

1. **Exportar a tabela inteira** da sua área:
   - Resultado da consulta vem paginado
   - "Exportar Excel" no canto superior

2. **Web scraping** (cuidado com termos de uso):
   - Use seletores HTML estáveis
   - Respeite rate limit (1 req/seg)

3. **Plataformas de terceiros** (não-oficiais):
   - https://qualis.capes.gov.br (instabilidade variável)
   - Periódicos do CAPES (apenas indica revistas indexadas, sem estrato)

---

## Dúvidas frequentes

### A revista não aparece?
- Pode ser que ela **não esteja classificada** na área que você escolheu
- Tente outra área (ex: revista interdisciplinar)
- Pode ser **revista nova** (sem histórico bibliométrico)
- Pode ser **predatória** (geralmente não classificada)

### Qual estrato vale: A1 numa área ou B1 noutra?
- **Use o da SUA área** (do PPG do trabalho)
- Se você é orientado num PPG de Educação e publica numa revista de saúde, vale o Qualis na Educação (a CAPES avalia o PPG-Educação)

### Qualis vs Fator de Impacto (JCR)?
- **Qualis** é métrica brasileira pra **avaliação de PPG**
- **JCR/SJR/CiteScore** são métricas internacionais bibliométricas
- A CAPES considera ambos no cálculo do Qualis
- Pra Lattes brasileiro, **Qualis é a referência**

### Mudou de quadriênio, e agora?
- O Qualis vigente **é sempre o último publicado**
- Trabalhos publicados em quadriênios anteriores **mantêm a classificação da época** pra fins de Lattes
- Pra avaliação de PPG, vale o vigente

---

## Atualização do Qualis (cronograma CAPES)

| Quadriênio | Vigência | Status |
|---|---|---|
| 2013-2016 | 2017-2018 | Antigo (não usar) |
| 2017-2020 | 2021-2025+ | **Vigente** |
| 2021-2024 | em discussão | Em consulta pública |

⚠️ Sempre verifique se o quadriênio mudou consultando a página oficial.

---

## Recursos complementares

- [Documentos de Área CAPES](https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao) — critérios detalhados por área
- [Beall's List](https://beallslist.net) — revistas predatórias
- [DOAJ](https://doaj.org) — revistas open access legítimas
- [SciELO](https://www.scielo.br) — revistas BR de qualidade
- [Periódicos CAPES](https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br) — base de busca via CAFe

---

## Fonte oficial

[CAPES — Plataforma Sucupira](https://sucupira.capes.gov.br)
