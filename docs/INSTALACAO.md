# Instalação — pesquisador-br-skill

Guia detalhado pra instalar a skill no Claude Code.

---

## Pré-requisitos

- **Claude Code** instalado e configurado
- **Git** instalado
- **Python 3.9+** (apenas se for usar os scripts utilitários)

---

## Método 1: via plugin marketplace (recomendado)

### Passo 1: Adicionar marketplace

No Claude Code, execute:

```bash
/plugin marketplace add https://github.com/SEU-USUARIO/pesquisador-br-skill
```

### Passo 2: Instalar plugin

```bash
/plugin install pesquisador-br-skill
```

### Passo 3: Reiniciar Claude Code

Saia do Claude Code e abra novamente. As skills serão detectadas automaticamente.

### Passo 4: Verificar instalação

Faça uma pergunta que ative a skill:

```
Como faço a estrutura de um TCC ABNT?
```

Se a skill `pesquisador-br` for invocada (você verá a notificação), está funcionando.

---

## Método 2: instalação manual (avançado)

### Passo 1: Clonar repositório

```bash
git clone https://github.com/SEU-USUARIO/pesquisador-br-skill.git
cd pesquisador-br-skill
```

### Passo 2: Copiar skills pra Claude Code

#### Linux / macOS
```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

#### Windows (PowerShell)
```powershell
$claudeSkills = "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Force -Path $claudeSkills
Copy-Item -Path .\skills\* -Destination $claudeSkills -Recurse
```

#### Windows (Git Bash)
```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

### Passo 3: Reiniciar Claude Code

Saia e abra novamente.

---

## Método 3: link simbólico (pra desenvolvimento)

Se você quer **editar a skill** e ver mudanças instantâneas (sem copiar a cada vez):

```bash
# Linux/macOS
ln -s "$(pwd)/skills/pesquisador-br" ~/.claude/skills/pesquisador-br
ln -s "$(pwd)/skills/revisao-sistematica-br" ~/.claude/skills/revisao-sistematica-br
ln -s "$(pwd)/skills/revisor-pares-br" ~/.claude/skills/revisor-pares-br
ln -s "$(pwd)/skills/tcc-abnt" ~/.claude/skills/tcc-abnt

# Windows (PowerShell, requer admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\pesquisador-br" -Target "$(pwd)\skills\pesquisador-br"
```

Agora qualquer mudança no diretório do projeto reflete na skill instalada.

---

## Configuração adicional

### Variáveis de ambiente (opcional)

Crie um arquivo `.env` na raiz do projeto pra configurar serviços externos:

```env
# Para integração com bases de dados acadêmicas
SCIELO_API_KEY=
PERIODICOS_CAPES_TOKEN=

# Para CrossRef (DOI → referência)
CROSSREF_USER_AGENT=pesquisador-br-skill/0.1 (mailto:seu@email.br)

# Para Anthropic API (caso queira usar Claude diretamente)
ANTHROPIC_API_KEY=
```

⚠️ **Nunca commite** esse arquivo no git. Está no `.gitignore`.

### Scripts Python

Pra usar os scripts utilitários (`scripts/busca_scielo.py`, `scripts/doi_para_referencia.py`):

```bash
# Verificar Python instalado
python --version  # ou python3 --version

# Rodar exemplo
python scripts/busca_scielo.py "ensino híbrido" --max 10
python scripts/doi_para_referencia.py 10.1590/S1413-24782020000100008
```

Não há dependências externas (usa stdlib).

---

## Troubleshooting

### Skill não é detectada

**Causa**: arquivo SKILL.md não está em `~/.claude/skills/<nome>/SKILL.md`.

**Solução**:
```bash
ls ~/.claude/skills/
# Deve mostrar: pesquisador-br/, revisao-sistematica-br/, ...

cat ~/.claude/skills/pesquisador-br/SKILL.md | head -10
# Deve mostrar o frontmatter com 'name' e 'description'
```

### Triggers não ativam a skill

**Causa**: o usuário não usou termos do `triggers` no SKILL.md.

**Solução**: tente com palavras-chave mais explícitas:
- "Me ajude com normas ABNT"
- "Preciso fazer um TCC"
- "Como estruturar dissertação de mestrado?"

Ou peça **explicitamente** pra invocar:
```
Use a skill pesquisador-br pra me ajudar com [tema]
```

### Plugin não instala (marketplace)

**Causa**: URL do repositório errada ou marketplace não configurado.

**Solução**:
```bash
# Listar marketplaces configurados
/plugin marketplace list

# Remover e adicionar de novo
/plugin marketplace remove pesquisador-br-skill
/plugin marketplace add https://github.com/SEU-USUARIO/pesquisador-br-skill
```

### Skill carregada mas comportamento estranho

**Causa**: Claude Code em cache antigo ou versão desatualizada.

**Solução**:
```bash
# Verificar versão Claude Code
claude --version

# Limpar cache (caminho varia por SO)
# Linux/macOS: ~/.cache/claude/
# Windows: %LOCALAPPDATA%\claude\Cache\

# Reiniciar Claude Code
```

---

## Atualização

### Atualizar via plugin

```bash
/plugin update pesquisador-br-skill
```

### Atualizar via git pull

```bash
cd /caminho/para/pesquisador-br-skill
git pull origin master
cp -r skills/* ~/.claude/skills/  # Se for instalação manual
```

---

## Desinstalação

### Via plugin
```bash
/plugin uninstall pesquisador-br-skill
```

### Manual
```bash
rm -rf ~/.claude/skills/pesquisador-br
rm -rf ~/.claude/skills/revisao-sistematica-br
rm -rf ~/.claude/skills/revisor-pares-br
rm -rf ~/.claude/skills/tcc-abnt
```

---

## Próximos passos

1. Leia [`docs/USO.md`](USO.md) pra ver exemplos de uso
2. Leia [`docs/ARQUITETURA.md`](ARQUITETURA.md) pra entender a estrutura
3. Conheça as referências de ABNT em [`skills/pesquisador-br/references/abnt/`](../skills/pesquisador-br/references/abnt/)
4. Experimente os scripts em [`scripts/`](../scripts/)

Bem-vindo à pesquisa acadêmica brasileira no Claude Code 🇧🇷
