# Changelog
Todas as mudanças notáveis do projeto SigTicket serão documentadas aqui.
O formato é baseado em Keep a Changelog.
---
## [1.0.0] - 2025-12-20
VERSÃO FINAL - ENTREGA DO PROJETO
### Adicionado
- Sistema completo de gerenciamento de tickets
- Autenticação de usuários com múltiplos perfis
- Criação de tickets com validação completa
- Listagem de todos os tickets
- Alteração de status com validação
- Sistema de relatórios
- Documentação técnica completa (DOCS.md)
- Comentários explicativos em todo o código
- Docstrings em todas as funções
### Melhorado
- Código completamente documentado
- Mensagens de erro mais descritivas
- Validações robustas
- Organização do código em módulos
---
## [0.4.0] - 2025-12-19
### Adicionado
- Documentação técnica completa (DOCS.md)
- Comentários explicativos em todo o código
- Docstrings detalhadas em todas as funções
- Cabeçalho com informações do projeto
- Exemplos de uso em docstrings
### Melhorado
- Legibilidade do código
- Manutenibilidade
- Documentação inline
---
## [0.3.0] - 2025-12-18
### Adicionado
- Arquivo CHANGELOG.md para documentar mudanças
- Code review completo entre grupos
### Melhorado
- Mensagens de erro mais descritivas (code review)
- Constantes movidas para topo do arquivo
- Comentários adicionais no código
- Refatoração baseada em sugestões do code review
---
## [0.2.0] - 2025-12-17
### Adicionado
- Arquivo .gitignore para ignorar arquivos temporários
- Arquivo config.py para configurações centralizadas
- README.md com documentação completa do projeto
### Mudado
- Credenciais movidas de hardcoded para arquivo de configuração
- Suporte para múltiplos usuários (admin e suporte)
- Configurações centralizadas
### Segurança
- Remoção de senhas hardcoded do código principal
- Avisos de segurança no config.py
---
## [0.1.1] - 2025-12-16
### Corrigido
- Bug #2: Validação de data na criação de tickets
- Formato DD/MM/AAAA obrigatório
- Rejeita datas futuras
- Rejeita datas inválidas (ex: 32/13/2025)
- Limita tentativas de entrada (3 tentativas) 
- Valida campos obrigatórios
- Bug #1: Validação de status de tickets
- Lista de status válidos implementada
- Validação antes de alterar status
- Mensagens de erro claras
- Tratamento de exceções
---
## [0.1.0] - 2025-12-15
### Adicionado
- Auditoria técnica completa do sistema legado
- Issues criadas para bugs identificados (5 issues)
- Board Kanban no GitHub Projects
- Documentação inicial dos problemas encontrados
### Identificado
- Issue #1: Falta validação de status
- Issue #2: Falta validação de data
- Issue #3: Senha hardcoded no código
- Issue #4: Ausência de .gitignore
- Issue #5: README incompleto
---
## Legendas
- **Adicionado** - Novas funcionalidades
- **Mudado** - Mudanças em funcionalidades existentes
- **Descontinuado** - Funcionalidades que serão removidas
- **Removido** - Funcionalidades removidas
- **Corrigido** - Correção de bugs
- **Segurança** - Correções de vulnerabilidades
- **Melhorado** - Aprimoramentos de qualidade
