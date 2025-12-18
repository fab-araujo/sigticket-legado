# SigTicket - Sistema de Gerenciamento de Tickets
Sistema simples de tickets para gerenciar solicitações e problemas.
## �� Funcionalidades
- ✅ Criação de tickets com validação de dados
- ✅ Listagem de todos os tickets
- ✅ Alteração de status com validação
- ✅ Sistema de autenticação
- ✅ Validação de datas no formato DD/MM/AAAA
## �� Como Executar
### Pré-requisitos
- Python 3.8 ou superior
### Instalação
1. Clone o repositório:
git clone https://github.com/[seu-usuario]/sigticket.git
cd sigticket-[grupo]
2. Execute o sistema:
python tickets.py
### Login
**Usuários disponíveis:**
- Usuário: `admin` / Senha: `admin123`
- Usuário: `suporte` / Senha: `suporte123`
## �� Como Usar
### Menu Principal
1. **Criar Ticket** - Cadastra novo ticket com título, descrição, usuário e data
2. **Listar Tickets** - Exibe todos os tickets cadastrados
3. **Mudar Status** - Altera status de um ticket existente
4. **Ver Relatório** - Exibe estatísticas dos tickets
5. **Sair** - Encerra o sistema
### Status Válidos
- `aberto` - Ticket recém-criado
- `em_andamento` - Ticket sendo resolvido
- `resolvido` - Problema solucionado
- `fechado` - Ticket finalizado
### Formato de Data
Use sempre o formato **DD/MM/AAAA**
Exemplos válidos: `15/12/2025`, `01/01/2024`
## ��️ Estrutura do Projeto
sigticket/
├── tickets.py # Código principal do sistema
├── config.py # Configurações e credenciais
├── .gitignore # Arquivos ignorados pelo Git
├── README.md # Este arquivo
└── CHANGELOG.md # Histórico de mudanças
## �� Correções Realizadas
- **Bug #1:** Validação de status de tickets
- **Bug #2:** Validação de formato de data
- **Refatoração:** Remoção de senha hardcoded
## �� Equipe
- [Elias Roberto da Cruz Pinto]
- [João Marcos Pinto da Cruz Moura]
## �� Projeto
Trabalho da disciplina Engenharia de Software II
Data: Dezembro/2025
## �� Licença
Projeto acadêmico - Uso educacional
