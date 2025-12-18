"""
Arquivo de configuração do sistema SigTicket.
NÃO COMMITAR SENHAS REAIS EM PRODUÇÃO!
"""

# Credenciais de acesso (apenas para ambiente de desenvolvimento)
USUARIOS = {
    "admin": "admin123",
    "suporte": "suporte123"
}

# Configurações do sistema
STATUS_VALIDOS = ["aberto", "em_andamento", "resolvido", "fechado"]
MAX_TENTATIVAS_DATA = 3
ANO_MINIMO = 2000
