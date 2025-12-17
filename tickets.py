"""
SigTicket - Sistema de Gestão de Tickets de Suporte
Versão Corrigida (NAP 2 - Correção de Bugs)
"""

from datetime import datetime
from config import USUARIOS, STATUS_VALIDOS

# Base de dados em memória
tickets = []


def menu_principal():
    print("\n" + "=" * 50)
    print("       SIGTICKET - Sistema de Tickets")
    print("=" * 50)
    print("1. Criar novo ticket")
    print("2. Listar todos os tickets")
    print("3. Mudar status de um ticket")
    print("4. Buscar ticket por ID")
    print("5. Sair")
    print("=" * 50)

# BUG #2 – VALIDAÇÃO DE DATA

def criar_ticket():
    print("\n=== CRIAR TICKET ===")

    titulo = input("Título: ").strip()
    if not titulo:
        print("✗ Título obrigatório")
        return

    descricao = input("Descrição: ").strip()
    if not descricao:
        print("✗ Descrição obrigatória")
        return

    usuario = input("Usuário: ").strip()
    if not usuario:
        print("✗ Usuário obrigatório")
        return

    for tentativa in range(3):
        data = input("Data (DD/MM/AAAA): ").strip()
        valida, msg = validar_data(data)

        if valida:
            data = msg
            break
        else:
            print(f"✗ {msg}")
            if tentativa < 2:
                print(f"  Tentativas restantes: {2-tentativa}")

    if not valida:
        print("✗ Máximo de tentativas. Cancelado.")
        return

    novo_ticket = {
        "id": len(tickets) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "usuario": usuario,
        "data": data,
        "status": "aberto"
    }

    tickets.append(novo_ticket)
    print(f"✓ Ticket #{novo_ticket['id']} criado!")

def listar_tickets():
    if not tickets:
        print("\nNenhum ticket cadastrado.")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'Título':<30} {'Status':<15} {'Data':<12}")
    print("=" * 80)

    for t in tickets:
        print(f"{t['id']:<5} {t['titulo']:<30} {t['status']:<15} {t['data']:<12}")

    print("=" * 80)
    print(f"Total: {len(tickets)} ticket(s)")


# BUG #1 – VALIDAÇÃO DE STATUS

def mudar_status():
    """Altera status com validação."""
    # Agora usa STATUS_VALIDOS do config.py
    listar_tickets()
    
    try:
        ticket_id = int(input("\nID do ticket: "))
    except ValueError:
        print("✗ ID inválido")
        return

    print("\nStatus válidos:")
    for s in STATUS_VALIDOS:
        print(f" - {s}")

    novo_status = input("\nNovo status: ").strip().lower()

    if novo_status not in STATUS_VALIDOS:
        print(f"✗ Status inválido! Use: {', '.join(STATUS_VALIDOS)}")
        return

    for t in tickets:
        if t["id"] == ticket_id:
            t["status"] = novo_status
            print(f"✓ Status alterado para: {novo_status}")
            return

    print("✗ Ticket não encontrado")


def buscar_ticket(ticket_id):
    for t in tickets:
        if t["id"] == ticket_id:
            print("\n" + "=" * 50)
            print(f"TICKET #{t['id']}")
            print("=" * 50)
            print(f"Título:      {t['titulo']}")
            print(f"Descrição:   {t['descricao']}")
            print(f"Usuário:     {t['usuario']}")
            print(f"Data:        {t['data']}")
            print(f"Status:      {t['status']}")
            print("=" * 50)
            return

    print("✗ Ticket não encontrado")

def fazer_login():
    """Realiza login do usuário."""
    print("\n=== LOGIN ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        print(f"✓ Login realizado: {usuario}")
        return True
    else:
        print("✗ Usuário ou senha inválidos")
        return False

def main():
    print("\n🎫 Bem-vindo ao SigTicket!")

    if not fazer_login():
        print("Acesso negado.")
        return

    while True:
        menu_principal()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            criar_ticket()

        elif opcao == "2":
            listar_tickets()

        elif opcao == "3":
            mudar_status()

        elif opcao == "4":
            try:
                tid = int(input("\nID do ticket: "))
                buscar_ticket(tid)
            except ValueError:
                print("✗ ID inválido")

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("✗ Opção inválida!")


# Dados de teste (opcional)
def carregar_dados_teste():
    tickets.extend([
        {
            "id": 1,
            "titulo": "Impressora não funciona",
            "descricao": "A impressora do 3º andar está offline",
            "usuario": "joao.silva",
            "data": "01/12/2025",
            "status": "aberto"
        }
    ])


if __name__ == "__main__":
    carregar_dados_teste()
    main()