# Como Usar — pesquisador-br-skill

Guia prático com exemplos reais.

---

## 🎬 Exemplo 1: Começando um TCC do zero

```
Você: Vou fazer meu TCC sobre uso de IA generativa no ensino superior.
Sou aluna de Pedagogia da UFAM. Não sei por onde começar.

iRMÃO (skill pesquisador-br ativa): 
Olá! Vou te ajudar.

Pra calibrar bem, me responde:
1. Área CAPES: Educação? (parece ser Pedagogia, área 70800006)
2. Tipo de trabalho: TCC graduação
3. Em que etapa estamos: tema bruto
4. Prazo: ?
5. Você já tem orientador?

Você: Sim, é Educação. TCC graduação. Tema bruto. Prazo: 6 meses.
Tenho orientadora.

iRMÃO: Beleza. Próximo passo: refinar o tema.

"Uso de IA generativa no ensino superior" é um tema amplo. Pra TCC,
recomendo recortar:

Opções de recorte:
1. **Sujeito**: estudantes? professores? gestores?
2. **Tipo de IA**: ChatGPT? geral? pra tarefas específicas?
3. **Disciplina/curso**: licenciatura? especifico em Pedagogia?
4. **Recorte temporal**: pós-pandemia? últimos 2 anos?
5. **Foco**: como usam? percepções? efeitos no aprendizado?
6. **Método**: estudo de caso? survey? análise documental?

Me responde 2-3 dessas pra eu te ajudar a fechar o problema de
pesquisa.
```

---

## 🎬 Exemplo 2: Convertendo APA → ABNT

```
Você: Tenho um texto em APA, preciso converter pra ABNT. Trecho:

"According to Smith (2020, p. 45), 'the impact of technology...'.
This view is also supported by Jones et al. (2021)."

References:
- Smith, J. (2020). Title. Journal Name, 12(3), 45-67.
- Jones, A., Brown, B., & Davis, C. (2021). Other title. Another
  Journal, 5(2), 78-90.

Use modo format-convert.

iRMÃO: 
Convertido pra ABNT 6023:2018 + 10520:2023:

**No texto:**
"Conforme Smith (2020, p. 45), 'the impact of technology...'. Essa
visão é também sustentada por Jones, Brown e Davis (2021)."

(observação: 3 autores → todos listados na primeira menção)

**Nas referências:**
SMITH, J. Title. **Journal Name**, v. 12, n. 3, p. 45-67, 2020.

JONES, A.; BROWN, B.; DAVIS, C. Other title. **Another Journal**,
v. 5, n. 2, p. 78-90, 2021.

⚠️ Verifique:
1. Faltou cidade da publicação (campo "Local")
2. Adicione DOI se houver
3. Se for online, adicione "Disponível em: URL. Acesso em: data."

Me passa esses dados que completo a referência.
```

---

## 🎬 Exemplo 3: Revisão sistemática

```
Você: Preciso fazer revisão sistemática sobre ensino híbrido em
educação superior brasileira.

iRMÃO (skill revisao-sistematica-br ativa):
Show. Vou te conduzir pela RS.

**Etapa 1: Definir pergunta PICO**

Sugestão:
- P: Estudantes universitários brasileiros
- I: Ensino híbrido (presencial + online)
- C: Ensino exclusivamente presencial OU exclusivamente remoto
- O: Desempenho acadêmico, satisfação, evasão

Pergunta final: "Como o ensino híbrido tem afetado [outcome] de 
estudantes universitários brasileiros, em comparação com modelos
exclusivamente presenciais ou remotos?"

Você concorda com esse PICO? Quer ajustar algo?

**Etapa 2: Critérios de inclusão/exclusão**

Sugestão:
- Inclusão: 
  - Período: 2018-2026
  - Idiomas: PT, EN
  - Tipo: artigos científicos peer-reviewed
  - Bases: SciELO, Periódicos CAPES, BDTD
  - Foco: educação superior (excluir EJA, médio)
  
- Exclusão:
  - Editoriais, opiniões sem dados
  - Estudos antes de 2018
  - Outros níveis de ensino

OK?

**Etapa 3: Strings de busca**

Vou montar pra cada base:

SciELO:
("ensino híbrido" OR "blended learning" OR "ensino misto")
AND ("educação superior" OR "ensino superior" OR "graduação"
OR "universidade")

Periódicos CAPES (Scopus):
("blended learning" OR "hybrid teaching" OR "hybrid learning")
AND ("higher education" OR "undergraduate")
AND (Brazil OR Brasil)

BDTD:
("ensino híbrido" OR "blended learning") AND ("educação superior")

Pode rodar essas buscas? Me traz os números (quantos resultados
em cada base) que dou os próximos passos.
```

---

## 🎬 Exemplo 4: Revisão ABNT de texto

```
Você: Pode revisar este parágrafo do meu TCC pra ABNT?

"Eu acredito que a metodologia qualitativa é melhor pra pesquisas
em educação. Conforme Bardin a análise de conteúdo tem 3 etapas. 
Esse método foi usado em vários trabalhos como o de Silva e Costa
2020, que mostraram que..."

iRMÃO (skill pesquisador-br modo revision):

📋 **Revisão ABNT do parágrafo**

### Problemas identificados

**1. Impessoalidade ❌**
- "Eu acredito" → não usar 1ª pessoa
- Sugestão: "Considera-se que" ou "Argumenta-se que"

**2. Citação NBR 10520 ❌**
- "Conforme Bardin" → falta ano: "Conforme Bardin (2011)"
- "como o de Silva e Costa 2020" → falta vírgula e parênteses:
  "como o de Silva e Costa (2020)" ou "(SILVA; COSTA, 2020)"

**3. Citação direta sem aspas ❌**
- "a análise de conteúdo tem 3 etapas" — se isso é citação direta
  de Bardin, precisa de aspas + página

**4. Conteúdo: pouco específico ⚠️**
- Quais são as 3 etapas? Citar concretamente

### Versão revisada (proposta)

"Considera-se que a abordagem qualitativa é mais adequada para
pesquisas em educação. Conforme Bardin (2011), a Análise de
Conteúdo organiza-se em três etapas: pré-análise, exploração do
material e tratamento dos resultados. Esse método tem sido
amplamente adotado em estudos brasileiros — como em Silva e Costa
(2020), que demonstraram [...]."

### Anota pra próxima vez
- ✅ Use voz passiva sintética: "considera-se", "argumenta-se"
- ✅ Toda citação precisa de (AUTOR, ANO)
- ✅ Citação direta SEMPRE com aspas e página

Quer que eu reveja outros parágrafos?
```

---

## 🎬 Exemplo 5: Resposta a parecer (R&R)

```
Você: Recebi este parecer de revisor da RBE:
"O autor não dialoga com a literatura recente sobre o tema. Os
trabalhos de Costa (2023) e Pereira (2024) deveriam ser
considerados. Além disso, a metodologia carece de rigor: como foi
feita a análise dos dados qualitativos?"

Como respondo formalmente?

iRMÃO:

📝 Carta de Resposta a Revisor (R&R)

---

**Sr(a). Editor(a) Chefe**

Agradecemos as valiosas contribuições do(a) revisor(a). Abaixo
respondemos a cada ponto, indicando as alterações realizadas no
manuscrito.

---

**Comentário 1: "O autor não dialoga com a literatura recente"**

**Resposta**: Agradecemos pela observação. Concordamos com a
crítica e ampliamos o referencial teórico (seção 2.3, p. 8-10)
para incluir os trabalhos de Costa (2023) e Pereira (2024),
estabelecendo diálogo crítico com seus achados. Especificamente:

- Costa (2023) reforça nosso argumento sobre [X], como discutido
  no parágrafo 3 da página 9.
- Pereira (2024), em contrapartida, oferece perspectiva alternativa,
  o que nos levou a refinar a hipótese H2, agora mais
  cuidadosamente formulada (p. 11).

**Comentário 2: "Metodologia carece de rigor: como foi feita a
análise qualitativa?"**

**Resposta**: Concordamos que a descrição metodológica estava
sucinta. Reescrevemos a seção 3.4 (p. 14-15), detalhando:

(a) **Procedimento de análise**: adotou-se o método de Análise
de Conteúdo (BARDIN, 2011), em três etapas — pré-análise,
exploração do material e tratamento dos resultados.

(b) **Categorização**: a partir do corpus de [X] entrevistas, 
emergiram [N] categorias temáticas, a saber: [...].

(c) **Confiabilidade**: a categorização foi validada por dois
pesquisadores independentes, com índice de concordância
inter-avaliadores de Kappa = [valor], considerado [substancial/
moderado] segundo Landis e Koch (1977).

(d) **Software**: utilizou-se o NVivo 12 para organização dos
dados.

Esperamos que as revisões realizadas atendam às pertinentes
sugestões.

Atenciosamente,
[Autores]
```

---

## 🎬 Exemplo 6: Verificar Qualis de revista

```
Você: A revista que estou pensando submeter é "Cadernos de Saúde
Pública". É Qualis A?

iRMÃO:

🔍 **Verificação Qualis CAPES**

Cadernos de Saúde Pública (CSP)

- **Mantenedora**: Fiocruz / ENSP
- **ISSN**: 0102-311X (impresso) / 1678-4464 (online)
- **Open access**: Sim (SciELO + site próprio)
- **Indexação**: Scopus, Web of Science, MEDLINE/PubMed, SciELO

**Qualis 2017-2020 (vigente)**:

| Área de Avaliação | Estrato |
|---|---|
| Saúde Coletiva | A1 ⭐ |
| Medicina I | A2 |
| Medicina II | A3 |
| Enfermagem | A1 |
| Educação Física | A2 |

**Veredicto**: ✅ **EXCELENTE escolha**. A1 em Saúde Coletiva
(área principal de revistas de saúde pública).

**Pra confirmar (e ver outras áreas)**:
https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf

Filtra por:
- Evento: Quadriênio 2017-2020
- Área: Saúde Coletiva (40500001)
- ISSN: 0102-311X

⚠️ **Cuidado**: A1 também é altamente competitivo. Tempo médio de
avaliação: 8-15 meses. Considere submeter versão pré-print no
arXiv/SciELO Preprints enquanto aguarda.
```

---

## 🎬 Exemplo 7: Disclosure de IA

```
Você: Como faço a disclosure de uso de IA no meu trabalho?

iRMÃO (modo disclosure):

📜 **Declaração de Uso de IA Generativa**

Modelo padrão (recomendado pela CAPES e comitês de ética):

---

**DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL**

Os autores declaram que utilizaram ferramentas de Inteligência
Artificial generativa no desenvolvimento deste trabalho, conforme
detalhado abaixo:

| Etapa | Ferramenta | Uso específico |
|---|---|---|
| Revisão de literatura | Claude (Anthropic) | Sugestão de bases de dados e refinamento de strings de busca |
| Redação | Claude / ChatGPT | Auxílio na revisão linguística e organização de parágrafos |
| Análise de dados | Não foi utilizada IA | — |
| Conceitos e argumentos centrais | Não foi utilizada IA | — |

Os autores afirmam que:

(a) Todas as ideias, argumentos, análises e conclusões apresentadas
são de autoria própria;

(b) A IA foi utilizada apenas como ferramenta auxiliar de
produtividade, equivalente a um corretor ortográfico avançado ou
gestor de referências;

(c) Não foram utilizadas IAs para fabricar, modificar ou inferir
dados de pesquisa, conclusões ou resultados;

(d) Todas as referências bibliográficas foram verificadas
manualmente em suas fontes originais antes da inclusão;

(e) A revisão final do manuscrito foi realizada integralmente
pelos autores, sem dependência de outputs automatizados.

[Local], [data].
[Assinatura dos autores]

---

⚠️ **Adapte conforme o uso real que você fez**.

Algumas revistas pedem:
- Declaração específica no submission
- Box separado no artigo
- Tabela CRediT modificada com "IA assistance"

Verifique normas da revista alvo.
```

---

## 🎯 Comandos rápidos pra invocar

A skill ativa quando você usa palavras-chave. Os mais eficazes:

| Você diz | Ativa skill |
|---|---|
| "ABNT" / "norma brasileira" | pesquisador-br |
| "TCC" / "monografia" / "dissertação" / "tese" | pesquisador-br ou tcc-abnt |
| "artigo científico em português" | pesquisador-br |
| "Qualis CAPES" / "estrato Qualis" | pesquisador-br |
| "SciELO" / "Lattes" / "BDTD" | pesquisador-br |
| "revisão sistemática" / "PRISMA" / "metanálise" | revisao-sistematica-br |
| "revisão por pares" / "parecer" | revisor-pares-br |
| "TCC ABNT completo" | tcc-abnt |

---

## 💡 Dicas

1. **Forneça contexto no início**: área CAPES + tipo de trabalho + estrato Qualis = calibração precisa.

2. **Não confie cegamente**: a skill orienta, mas **você é o(a) pesquisador(a)**. Confira tudo.

3. **Use o modo certo**:
   - `plan` antes de escrever
   - `revision` depois de escrever
   - `format-convert` pra adaptar texto entre normas
   - `disclosure` pra declaração de IA

4. **Pra citações reais**: use `scripts/doi_para_referencia.py` ou `scripts/busca_scielo.py` pra evitar alucinação.

5. **Antes de submeter**: rode `citation-check` e revisão por pares simulada (`revisor-pares-br`).
