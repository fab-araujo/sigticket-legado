#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SigTicket - Sistema de Gerenciamento de Tickets
Versão: 1.0.0
Data: Dezembro/2025

Descrição:
Sistema simples para gerenciamento de tickets de suporte.
Permite criar, listar, buscar e alterar status de tickets com validações.

Autores:
[Elias roberto da Cruz Pinto]
[João Marcos Pinto da Cruz Moura]

Disciplina: Engenharia de Software II
"""

# ==============================
# Imports
# ==============================
from datetime import datetime

# ==============================
# Configurações simuladas (config.py embutido)
# ==============================
USUARIOS = {
    "admin": "admin123",
    "suporte": "suporte123"
}

STATUS_VALIDOS = ["aberto", "em_andamento", "fechado"]

# ==============================
# Base de dados em memória
# ==============================
tickets = []

# ==============================
# Funções de interface
# ==============================

def menu_principal():
    """
    Exibe o menu principal do sistema.
    """
    print("\n" + "=" * 50)
    print("       SIGTICKET - Sistema de Tickets")
    print("=" * 50)
    print("1. Criar novo ticket")
    print("2. Listar todos os tickets")
    print("3. Mudar status de um ticket")
    print("4. Buscar ticket por ID")
    print("5. Sair")
    print("=" * 50)


def fazer_login():
    """
    Realiza autenticação simples do usuário.

    Returns:
        bool: True se login válido, False caso contrário
    """
    print("\n=== LOGIN ===")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        print(f"✓ Login realizado: {usuario}")
        return True

    print("✗ Usuário ou senha inválidos")
    return False


# ==============================
# Funções de validação
# ==============================

def validar_data(data_str):
    """
    Valida se uma string representa uma data válida no formato DD/MM/AAAA.

    Regras:
    - Deve seguir o formato DD/MM/AAAA
    - Não aceita datas inválidas (ex: 31/02/2025)
    - Não aceita datas futuras
    - Não aceita datas anteriores ao ano 2000

    Args:
        data_str (str): Data informada pelo usuário

    Returns:
        tuple (bool, str):
            True e data formatada se válida
            False e mensagem de erro se inválida
    """
    data_str = data_str.strip()

    # Validação básica de formato
    if len(data_str) != 10 or data_str[2] != "/" or data_str[5] != "/":
        return False, "Use formato DD/MM/AAAA"

    try:
        # Conversão para datetime
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")

        # Regra de negócio: data futura não permitida
        if data_obj > datetime.now():
            return False, "Data não pode ser futura"

        # Regra de negócio: ano mínimo
        if data_obj.year < 2000:
            return False, "Ano deve ser >= 2000"

        return True, data_obj.strftime("%d/%m/%Y")

    except ValueError:
        return False, "Data inválida"


# ==============================
# Funções de negócio
# ==============================

def criar_ticket():
    """
    Cria um novo ticket com validação completa dos dados.

    Validações:
    - Título obrigatório
    - Descrição obrigatória
    - Usuário obrigatório
    - Data válida (formato, calendário e regras de negócio)

    O usuário possui até 3 tentativas para informar uma data válida.
    """
    print("\n=== CRIAR TICKET ===")

    # Validação do título
    titulo = input("Título: ").strip()
    if not titulo:
        print("Erro: Título obrigatório")
        return

    # Validação da descrição
    descricao = input("Descrição: ").strip()
    if not descricao:
        print("Erro: Descrição obrigatória")
        return

    # Validação do usuário solicitante
    usuario = input("Usuário: ").strip()
    if not usuario:
        print("Erro: Usuário obrigatório")
        return

    # Validação da data (até 3 tentativas)
    for tentativa in range(3):
        data_input = input("Data (DD/MM/AAAA): ").strip()
        valida, msg = validar_data(data_input)

        if valida:
            data = msg
            break
        else:
            print(f"Erro: {msg}")
            if tentativa < 2:
                print(f" Tentativas restantes: {2 - tentativa}")
    else:
        print("Erro: Máximo de tentativas. Operação cancelada.")
        return

    # Criação do ticket
    novo_ticket = {
        "id": len(tickets) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "usuario": usuario,
        "data": data,
        "status": "aberto"
    }

    tickets.append(novo_ticket)
    print(f"\n✓ Ticket #{novo_ticket['id']} criado com sucesso!")


def listar_tickets():
    """
    Lista todos os tickets cadastrados.
    """
    if not tickets:
        print("\nNenhum ticket cadastrado.")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'Título':<30} {'Status':<15} {'Data':<12}")
    print("=" * 80)

    for t in tickets:
        print(f"{t['id']:<5} {t['titulo']:<30} {t['status']:<15} {t['data']:<12}")

    print("=" * 80)


def mudar_status():
    """
    Altera o status de um ticket existente.

    Regras:
    - ID deve existir
    - Novo status deve estar em STATUS_VALIDOS
    """
    listar_tickets()

    try:
        ticket_id = int(input("\nID do ticket: "))
    except ValueError:
        print("Erro: ID inválido")
        return

    print("\nStatus válidos:")
    for s in STATUS_VALIDOS:
        print(f" - {s}")

    novo_status = input("\nNovo status: ").strip().lower()

    if novo_status not in STATUS_VALIDOS:
        print(f"Erro: Status inválido! Use: {', '.join(STATUS_VALIDOS)}")
        return

    for t in tickets:
        if t["id"] == ticket_id:
            t["status"] = novo_status
            print(f"✓ Status alterado para: {novo_status}")
            return

    print("Erro: Ticket não encontrado")


def buscar_ticket(ticket_id):
    """
    Busca e exibe um ticket pelo ID.

    Args:
        ticket_id (int): Identificador do ticket
    """
    for t in tickets:
        if t["id"] == ticket_id:
            print("\n" + "=" * 50)
            print(f"TICKET #{t['id']}")
            print("=" * 50)
            print(f"Título:    {t['titulo']}")
            print(f"Descrição: {t['descricao']}")
            print(f"Usuário:   {t['usuario']}")
            print(f"Data:      {t['data']}")
            print(f"Status:    {t['status']}")
            print("=" * 50)
            return

    print("Erro: Ticket não encontrado")


def carregar_dados_teste():
    """
    Carrega tickets fictícios para testes.
    """
    tickets.extend([
        {
            "id": 1,
            "titulo": "Impressora não funciona",
            "descricao": "Offline",
            "usuario": "joao",
            "data": "01/12/2025",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Senha esquecida",
            "descricao": "Reset",
            "usuario": "maria",
            "data": "02/12/2025",
            "status": "em_andamento"
        }
    ])


# ==============================
# Função principal
# ==============================

def main():
    """
    Controla o fluxo principal do sistema.
    """
    print("\n🎫 Bem-vindo ao SigTicket!")

    if not fazer_login():
        print("Acesso negado.")
        return

    while True:
        menu_principal()
        opcao = input("\nEscolha: ")

        if opcao == "1":
            criar_ticket()
        elif opcao == "2":
            listar_tickets()
        elif opcao == "3":
            mudar_status()
        elif opcao == "4":
            try:
                buscar_ticket(int(input("ID: ")))
            except ValueError:
                print("Erro: ID inválido")
        elif opcao == "5":
            print("Encerrando sistema...")
            break
        else:
            print("Erro: Opção inválida!")


if __name__ == "__main__":
    carregar_dados_teste()
    main()
    # teste
