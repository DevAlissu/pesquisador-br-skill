# SciELO (Scientific Electronic Library Online)

> Biblioteca eletrônica brasileira/latina-americana de revistas científicas open access. Indexador essencial pra pesquisa em PT-BR.

## O que é

Programa coordenado pela **FAPESP** + **BIREME** + **CNPq** que disponibiliza revistas científicas de forma gratuita. Inclui:

- **SciELO Brasil** (mais de 300 revistas BR)
- **SciELO Saúde Pública**
- **SciELO Latam** (México, Argentina, Chile, Colômbia, Cuba, Peru, etc)
- **SciELO Books** (livros acadêmicos)

URL: https://www.scielo.br

---

## Por que importa

✅ **Open access total** — não precisa de assinatura
✅ **Peer review** garantido (todas as revistas indexadas passam por avaliação)
✅ **Métricas claras** (CiteScore, fator de impacto)
✅ **Em português, espanhol e inglês** (área central de pesquisa em PT-BR)
✅ **Indexada em Scopus** (a maioria) — pontua em rankings internacionais
✅ **Conteúdo de qualidade** — revistas predatórias **não estão** no SciELO

⚠️ Para muitos PPGs, **estar publicado no SciELO já é um sinal de qualidade** (Qualis B2 ou superior em geral).

---

## Como buscar

### Busca simples
1. Acesse https://search.scielo.org
2. Digite termo
3. Filtre por:
   - **Coleção** (Brasil, Latam, etc)
   - **Idioma**
   - **Área temática**
   - **Periódico** específico
   - **Tipo de documento** (artigo, editorial, resenha)

### Busca avançada
- Operadores booleanos: AND, OR, NOT
- Por autor, título, resumo, descritor
- Por DOI

### Exemplos

```
Educação especial AND tecnologia
"análise de conteúdo" AND Bardin
au:(Minayo) AND ti:(qualitativa)
```

---

## API SciELO

Há duas APIs públicas:

### ArticleMeta API (REST/JSON)

Endpoint base: `https://articlemeta.scielo.org/api/v1/`

Endpoints:
- `/journal/?collection=scl` — listar revistas brasileiras
- `/journal/?issn=XXXX-XXXX` — info de uma revista
- `/article/?code=XXXXX` — info de um artigo
- `/issue/?issn=XXXX-XXXX` — issues de uma revista

Documentação: https://articlemeta.scielo.org/api/v1/

### OAI-PMH (harvesting)

URL: `https://www.scielo.br/oai/scielo-oai.php`

Padrão de protocolo de coleta acadêmica. Útil pra agregadores.

---

## Critérios de indexação SciELO

Pra uma revista entrar no SciELO BR, ela precisa:

1. **Periodicidade regular** (mínimo 4 fascículos/ano em geral)
2. **Peer review** duplo-cego documentado
3. **Conselho editorial qualificado** (com diversidade institucional e geográfica)
4. **Política antiplágio** explícita
5. **Política open access** (CC-BY ou similar)
6. **DOI** em todos os artigos
7. **Indicadores bibliométricos mínimos** (citação)
8. **Avaliação trianual** (entra/sai do SciELO)

⚠️ Revista sair do SciELO é golpe de credibilidade.

---

## Métricas SciELO

Cada revista tem página com:
- **CiteScore** (Scopus)
- **JCR Impact Factor** (se for indexada na WoS)
- **SJR** (Scimago Journal Rank)
- **h5-index** (Google Scholar)
- **Cited Half-Life**

Útil pra escolher onde submeter.

---

## Submeter um artigo

### 1. Identifique a revista certa
- Filtre por área temática
- Verifique escopo (apenas saúde? apenas educação?)
- Cheque Qualis na sua área CAPES

### 2. Leia "Diretrizes para autores"
Cada revista SciELO tem normas específicas:
- Tamanho do artigo
- Estilo de citação (NBR? Vancouver? APA?)
- Formato de tabelas/figuras
- Sistema de submissão (geralmente OJS)

### 3. Submeta via plataforma OJS da revista
- A maioria usa **OJS (Open Journal Systems)**
- URL típica: https://nome-revista.scielo.br/journal/manager
- Cadastre-se → Submeta

### 4. Acompanhe o processo
- Em revisão (peer review): geralmente 60-180 dias
- Decisão: aceito, aceito com revisões, rejeitado
- R&R (Revise & Resubmit): segunda rodada

---

## Citação ABNT de artigo SciELO

```
SOBRENOME, Nome. **Título do artigo**: subtítulo. *Nome da Revista*,
[s.l.], v. X, n. Y, p. ZZ-WW, mês ano. DOI: doi.
Disponível em: https://www.scielo.br/scielo.php?script=...
Acesso em: dia mês ano.
```

Exemplo:
```
MINAYO, Maria Cecília de Souza. Análise qualitativa: teoria, passos
e fidedignidade. *Ciência & Saúde Coletiva*, [s.l.], v. 17, n. 3,
p. 621-626, mar. 2012.
DOI: 10.1590/S1413-81232012000300007.
Disponível em: https://www.scielo.br/scielo.php?script=sci_arttext
&pid=S1413-81232012000300007. Acesso em: 15 abr. 2026.
```

⚠️ Note: títulos de artigos em **negrito** ou *itálico*; nomes de revistas em *itálico*.

---

## SciELO Books

URL: https://books.scielo.org

Livros acadêmicos open access em PT/ES/EN. Útil pra:
- Citar livros clássicos brasileiros
- Acessar Boaventura, Milton Santos, Paulo Freire, Florestan Fernandes etc

---

## SciELO Saúde Pública

URL: https://www.scielosp.org

Coleção temática focada em saúde pública. Inclui:
- *Cadernos de Saúde Pública* (FIOCRUZ)
- *Revista de Saúde Pública* (USP)
- *Ciência & Saúde Coletiva*
- + revistas latam de saúde

---

## SciELO Preprints

URL: https://preprints.scielo.org

Servidor de preprints pra publicação rápida ANTES de peer review. Útil pra:
- Compartilhar resultados rapidamente
- Receber feedback prévio
- Marcar prioridade científica
- Acelerar disseminação durante crises (COVID-19 mostrou utilidade)

⚠️ Preprint **não substitui** publicação peer-reviewed pra fins de Lattes/Qualis.

---

## Erros frequentes ao usar SciELO

❌ Confundir SciELO BR com SciELO Latam (revistas distintas)
❌ Não verificar Qualis da revista antes de submeter
❌ Submeter pra revista fora do escopo (vai ser rejeitada)
❌ Citar SciELO sem DOI
❌ Confundir SciELO com revista predatória de outro país (algumas pirateiam o nome)

---

## Recursos

- [SciELO Brasil](https://www.scielo.br)
- [SciELO Latam](https://search.scielo.org)
- [SciELO Books](https://books.scielo.org)
- [SciELO Preprints](https://preprints.scielo.org)
- [ArticleMeta API](https://articlemeta.scielo.org/api/v1/)
- [Critérios de indexação](https://www.scielo.br/avaliacao/avaliacao_pt.htm)
