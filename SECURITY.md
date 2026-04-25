# Política de Segurança

Obrigado pela atenção em manter o `pesquisador-br-skill` seguro para a comunidade acadêmica brasileira.

## Versões com suporte de segurança

| Versão | Suporte |
|---|---|
| 0.1.x | ✅ patches de segurança |
| < 0.1 | ❌ não suportado |

## Como reportar uma vulnerabilidade

**Não abra issue pública** para vulnerabilidades de segurança. Use um dos canais privados abaixo.

### Canal preferencial: GitHub Security Advisories

1. Acesse https://github.com/DevAlissu/pesquisador-br-skill/security/advisories/new
2. Preencha o formulário descrevendo a vulnerabilidade
3. O mantenedor é notificado privadamente

### Canal alternativo: e-mail

Envie para **alison.silva8741@gmail.com** com:

- Descrição da vulnerabilidade
- Passos para reproduzir
- Impacto observado ou potencial
- Versão afetada (commit hash ou release)
- Sua identificação (opcional, para crédito no patch)

Use o assunto: `[SECURITY] pesquisador-br-skill: <breve descrição>`.

## Tempo de resposta

| Etapa | Prazo alvo |
|---|---|
| Confirmação de recebimento | até **3 dias úteis** |
| Avaliação inicial e severidade | até **7 dias** |
| Patch + release | depende da gravidade (crítica: ≤ 14 dias; alta: ≤ 30 dias; média: próximo ciclo) |

## Escopo

### Em escopo

- Scripts Python em `scripts/`
- Workflows GitHub Actions em `.github/workflows/`
- Manifestos do plugin (`.claude-plugin/*.json`)
- Conteúdo dos templates LaTeX (em particular, vetores como `\write18`, `\input`, etc)
- Vetores de prompt-injection que comprometam o pipeline (ex: bypass de Integrity Gate, exfiltração de citação fabricada)

### Fora de escopo

- Vulnerabilidades em dependências do Claude Code (reportar à Anthropic)
- Vulnerabilidades em endpoints externos (SciELO, BDTD, CrossRef, IBICT — reportar aos respectivos mantenedores)
- Comportamentos do modelo Claude que não envolvam exploração técnica do plugin

## Limitações conhecidas

Documentadas explicitamente para evitar duplicidade de reports:

- **`busca_bdtd.py --endpoint <url>` com URL externa não-confiável**: a validação cobre os principais vetores SSRF (esquemas, IPs literais, IPv4-mapped IPv6, DNS rebinding via `getaddrinfo`, redirect chain), mas **não elimina TOCTOU** entre validação e request real. Mitigação completa via conexão por IP literal + `Host` header planejada para v0.2.0. Recomenda-se usar os aliases internos (`ufrgs`, `usp`, `ufmg`, `bdtd`).

## Disclosure responsável

Comprometemo-nos a:

- Confirmar recebimento e classificar severidade dentro do prazo
- Manter você informado sobre o progresso
- Creditar você no commit/changelog se desejar
- Coordenar disclosure público após o patch estar disponível

Pedimos que você:

- Não explore a vulnerabilidade além do necessário para demonstração
- Não compartilhe publicamente até o patch estar disponível
- Não acesse, modifique ou exfiltre dados de terceiros

## Histórico de patches de segurança

Registrado no [CHANGELOG.md](CHANGELOG.md) sob a seção `### 🛡️ Segurança` de cada versão.

---

Obrigado por contribuir com a segurança da pesquisa acadêmica brasileira.
