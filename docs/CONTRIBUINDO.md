# Contribuindo — pesquisador-br-skill

Toda contribuição é bem-vinda. Esta skill é construída pela comunidade brasileira de pesquisa, pra comunidade brasileira de pesquisa.

---

## Como você pode contribuir

### 1. Adicionar template
Tem um modelo de trabalho acadêmico que falta? Abra PR adicionando em `skills/pesquisador-br/templates/`.

Exemplos de templates desejados:
- Parecer de Banca de Qualificação
- Projeto FAPESP Auxílio Regular
- Relatório de PIBIC
- Projeto FAPEAM
- Carta de submissão a revista
- Disclosure de financiamento

### 2. Atualizar NBR
Quando uma nova versão de NBR sair (ex: NBR 14724:2025 quando vier), crie `nbr-XXXXX-2025.md` em `skills/pesquisador-br/references/abnt/`.

### 3. Adicionar revista da sua área
Em `skills/pesquisador-br/references/revistas/<sua-area>.md`, contribua com revistas Qualis A da sua área.

### 4. Reportar bug ou inconsistência
Encontrou erro em uma referência ABNT? Citação errada? Persona inadequada? Abra issue.

### 5. Traduzir docs
A skill é em PT-BR, mas docs podem ser traduzidas pra ES (mercado hispanofalante) ou EN (visibilidade internacional).

### 6. Validar academicamente
Se você é pesquisador(a) com PhD em alguma área e quer validar o conteúdo da skill na sua área, abra issue propondo revisão.

---

## Padrões de PR

### Branch
```
git checkout -b feat/template-projeto-fapesp
git checkout -b fix/nbr-6023-edicao-formato
git checkout -b docs/contribuindo-traducao-en
```

### Commit
- Em **português**
- Imperativo, presente
- Tipo + escopo + descrição

```
git commit -m "feat(template): adiciona projeto FAPESP Auxílio Regular"
git commit -m "fix(nbr-6023): corrige formato de edição em referências"
git commit -m "docs(uso): adiciona exemplo de revisão por pares"
```

### PR
- Título claro
- Descrição com contexto: o que mudou, por quê
- Vincule issues se aplicável
- Marque label apropriada

---

## Padrões de conteúdo

### Frontmatter de SKILL.md
```yaml
---
name: nome-da-skill
description: Descrição clara em PT-BR. Aciona quando [...]. Esta skill faz [...].
version: 0.1.0
language: pt-BR
related_skills:
  - outra-skill
triggers:
  - palavra-chave-1
  - palavra-chave-2
---
```

### Estrutura de template
- Markdown válido
- Cabeçalho com tipo de trabalho
- Estrutura completa (placeholders)
- Checklist final
- Exemplos quando útil

### Estrutura de reference (NBR, plataforma, autor)
- Origem oficial citada
- Exemplos práticos
- Erros comuns identificados
- Quando usar / quando não usar
- Cross-references com outros docs

### Voz da skill
- Direta, profissional
- Em PT-BR formal
- Sem firulas
- Sem "fofura artificial"
- Anti-padrão: "espero que isso te ajude!" → use: "Esses são os pontos."

---

## Checklist antes de PR

- [ ] Conteúdo está em **PT-BR**
- [ ] Não inventei referências (verifiquei na fonte)
- [ ] Não inventei normas (verifiquei na ABNT)
- [ ] Adicionei ao README ou docs (se aplicável)
- [ ] CI passou (workflows do `.github/workflows/`)
- [ ] Commits em PT-BR
- [ ] PR descrito com contexto

---

## Code of Conduct

- Respeito a todas as áreas do conhecimento
- Sem discriminação por área (Computação não é "superior" a Educação, por exemplo)
- Sem favoritismo por instituição/região
- Crítica deve ser construtiva e técnica
- Atribuir crédito quando usar trabalho de outros

---

## Contato

- Issues: https://github.com/SEU-USUARIO/pesquisador-br-skill/issues
- Discussões: https://github.com/SEU-USUARIO/pesquisador-br-skill/discussions

---

🇧🇷 Construindo a primeira skill brasileira pro Claude Code, juntos.
