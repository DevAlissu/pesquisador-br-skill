# Template: Diagrama de Fluxo PRISMA 2020

> Fluxograma obrigatório de qualquer RS conforme PRISMA 2020.
> Modelos em texto + ferramentas pra geração visual.

## Modelo PRISMA 2020 em texto/markdown

```
═══════════════════════════════════════════════════════════════
                        IDENTIFICAÇÃO
───────────────────────────────────────────────────────────────
                                                                
  Registros identificados nas bases:                            
  - SciELO Brasil: 145                                          
  - Periódicos CAPES (Scopus): 312                              
  - Web of Science: 198                                         
  - BDTD/IBICT: 67                                              
  - PubMed: 89                                                  
  - Cochrane: 23                                                
  TOTAL: 834                                                    
                                                                
  Registros identificados em outras fontes (manual):            
  - Citações de artigos relevantes: 12                          
  - Sugestão de especialistas: 5                                
                                                                
                    ↓                                           
                                                                
  Registros após remoção de duplicatas:                         
  TOTAL: 624                                                    
                                                                
═══════════════════════════════════════════════════════════════
                          TRIAGEM                               
───────────────────────────────────────────────────────────────
                                                                
  Registros triados por título e resumo:                        
  TOTAL: 624                                                    
                                                                
                    ↓                                           
                                                                
  Excluídos: 470                                                
   - Não atendem população: 145                                 
   - Não atendem intervenção: 89                                
   - Tipo de estudo inadequado: 178                             
   - Fora do período: 32                                        
   - Fora do idioma: 26                                         
                                                                
                    ↓                                           
                                                                
  Avaliados em texto completo:                                  
  TOTAL: 154                                                    
                                                                
═══════════════════════════════════════════════════════════════
                       ELEGIBILIDADE                            
───────────────────────────────────────────────────────────────
                                                                
  Excluídos por elegibilidade: 108                              
   - Sem desfecho de interesse: 42                              
   - Risco de viés crítico: 18                                  
   - Texto completo indisponível: 25                            
   - Duplicata não detectada antes: 8                           
   - Outros motivos: 15                                         
                                                                
                    ↓                                           
                                                                
═══════════════════════════════════════════════════════════════
                          INCLUSÃO                              
───────────────────────────────────────────────────────────────
                                                                
  Estudos incluídos na revisão sistemática:                     
  TOTAL: 46                                                     
                                                                
  Estudos incluídos na metanálise:                              
  TOTAL: 23 (subset com dados comparáveis)                      
                                                                
═══════════════════════════════════════════════════════════════
```

## Tabela de exclusões detalhada (apêndice obrigatório)

Liste **todos** os estudos excluídos no texto completo, com motivo específico:

| Estudo | Motivo de exclusão |
|---|---|
| Costa et al. (2018) | Sem desfecho de interesse |
| Silva (2019) | Texto completo indisponível |
| Pereira (2020) | Risco de viés crítico (NOS = 3/9) |
| Souza (2021) | Duplicata não detectada |
| ... | ... |

## Ferramentas pra gerar PRISMA visual

### Online (gratuitas)
- **PRISMA flow diagram generator** (Shiny app):
  https://estech.shinyapps.io/prisma_flowdiagram/
- **PRISMA 2020 flow diagram template** (Word):
  https://www.prisma-statement.org/PRISMAStatement/FlowDiagram

### Software
- **Microsoft Word** — usar caixas e setas
- **PowerPoint** — gerar e exportar como imagem
- **Lucidchart / Draw.io** — diagramas online
- **PRISMA R package** (R) — geração programática

## Versão LaTeX (para artigos científicos)

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[node distance=2cm, auto]
  \tikzstyle{block} = [rectangle, draw, fill=gray!10,
    text width=10em, text centered, rounded corners, minimum height=4em]
  
  \node [block] (id) {Identificação\\\textbf{N=834}};
  \node [block, below of=id] (dedup) {Após duplicatas\\\textbf{N=624}};
  \node [block, below of=dedup] (triagem) {Triagem\\\textbf{N=624}};
  \node [block, right of=triagem, xshift=4cm] (excl1) {Excluídos\\\textbf{N=470}};
  \node [block, below of=triagem, yshift=-1cm] (eleg) {Elegibilidade\\\textbf{N=154}};
  \node [block, right of=eleg, xshift=4cm] (excl2) {Excluídos\\\textbf{N=108}};
  \node [block, below of=eleg] (incl) {Incluídos\\\textbf{N=46}};
  
  \draw [->] (id) -- (dedup);
  \draw [->] (dedup) -- (triagem);
  \draw [->] (triagem) -- (eleg);
  \draw [->] (triagem) -- (excl1);
  \draw [->] (eleg) -- (incl);
  \draw [->] (eleg) -- (excl2);
\end{tikzpicture}
\caption{Diagrama PRISMA 2020 do processo de seleção}
\label{fig:prisma}
\end{figure}
```

## Princípios

✅ **Diagrama é obrigatório** em qualquer publicação RS PRISMA
✅ **Números devem fechar**: identificados − excluídos = incluídos em cada etapa
✅ **Liste motivos específicos** de exclusão (não "vários motivos")
✅ **Apresente apêndice** com lista completa de excluídos por motivo
✅ **Atualize PRISMA 2020** (não use versão antiga 2009)

❌ **Não invente números** pra fechar o diagrama
❌ **Não esconda exclusões** — transparência total
❌ **Não use diagrama esquemático** — siga o padrão PRISMA

## Onde inserir

- **No texto principal**: como Figura 1 da seção Resultados
- **Em apêndice**: tabela detalhada de exclusões
- **Como dado complementar**: planilha completa em repositório aberto (Zenodo, Figshare, OSF)
