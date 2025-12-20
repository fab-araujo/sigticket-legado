#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SigTicket - Sistema de Gerenciamento de Tickets
Versão: 1.0.0
Data: Dezembro/2025
Descrição:
Sistema simples para gerenciamento de tickets de suporte.
Permite criar, listar, buscar e alterar status de tickets com validações completas.
Autores:
Ed Hungria
[Emerson]
[Paulo]
[Alex]
Disciplina: Engenharia de Software II
"""

from datetime import datetime
from config import USUARIOS, STATUS_VALIDOS

# Base de dados em memória
tickets = []
contador_id = 1


def validar_data(data: str) -> bool:
    """
    Valida se a string 'data' está no formato DD/MM/AAAA e representa uma data válida,
    não futura e com ano a partir de 2000.
    
    Imprime mensagens de erro específicas e retorna True apenas se válida.
    """
    data = data.strip()
    
    # Verificações básicas de formato
    if len(data) != 10:
        print("✗ Erro: A data deve ter exatamente 10 caracteres (DD/MM/AAAA).")
        return False
    
    if data[2] != '/' or data[5] != '/':
        print("✗ Erro: A data deve usar '/' como separador (ex: 18/12/2025).")
        return False
    
    try:
        dia, mes, ano = map(int, data.split('/'))
    except ValueError:
        print("✗ Erro: Dia, mês e ano devem ser números.")
        return False
    
    # Validação com datetime
    try:
        data_obj = datetime(ano, mes, dia)
    except ValueError:
        print("✗ Erro: Data inválida! Verifique dia/mês (ex: 31/04 não existe).")
        return False
    
    # Rejeita datas futuras
    if data_obj.date() > datetime.now().date():
        print("✗ Erro: Data não pode ser futura.")
        return False
    
    # Rejeita anos muito antigos
    if ano < 2000:
        print("✗ Erro: Ano deve ser 2000 ou posterior.")
        return False
    
    return True


def menu_principal():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("       SIGTICKET - Sistema de Tickets")
    print("="*50)
    print("1. Criar novo ticket")
    print("2. Listar todos os tickets")
    print("3. Mudar status de um ticket")
    print("4. Buscar ticket por ID")
    print("5. Sair")
    print("="*50)


def validar_data(data_str):
    """
    Valida se uma string representa uma data válida no formato DD/MM/AAAA.
    
    Args:
        data_str (str): String contendo a data a ser validada
    
    Returns:
        tuple: (bool, str) onde:
            - bool: True se válida, False se inválida
            - str: Data formatada se válida, mensagem de erro se inválida
    """
    data_str = data_str.strip()
    if len(data_str) != 10 or data_str[2] != '/' or data_str[5] != '/':
        return False, "Use formato DD/MM/AAAA"
    try:
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")
        if data_obj > datetime.now():
            return False, "Data não pode ser futura"
        if data_obj.year < 2000:
            return False, "Ano deve ser >= 2000"
        return True, data_str
    except ValueError:
        return False, "Data inválida"


def criar_ticket():
    """
    Cria um novo ticket com validação completa dos campos.
    Validações: título, descrição, usuário obrigatórios; data válida com até 3 tentativas.
    """
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
    
    # Validação de data com 3 tentativas
    for tentativa in range(3):
        data = input("Data (DD/MM/AAAA): ").strip()
        valida, msg = validar_data(data)
        if valida:
            data = msg
            break
        else:
            print(f"✗ {msg}")
        if tentativa < 2:
            print(f" Tentativas restantes: {2 - tentativa}")
    else:
        print("✗ Máximo de tentativas. Operação cancelada.")
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
    """Lista todos os tickets cadastrados em formato tabular"""
    if not tickets:
        print("\nNenhum ticket cadastrado ainda.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Título':<30} {'Status':<15} {'Data':<12}")
    print("="*80)
    
    for t in tickets:
        print(f"{t['id']:<5} {t['titulo']:<30} {t['status']:<15} {t['data']:<12}")
    
    print("="*80)
    print(f"Total: {len(tickets)} ticket(s)")


def mudar_status():
    """
    Altera o status de um ticket existente com validação completa.
    Exibe lista de status válidos e rejeita entradas inválidas.
    """
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
    """Busca e exibe detalhes completos de um ticket específico pelo ID"""
    for t in tickets:
        if t["id"] == ticket_id:
            print("\n" + "="*50)
            print(f"TICKET #{t['id']}")
            print("="*50)
            print(f"Título:      {t['titulo']}")
            print(f"Descrição:   {t['descricao']}")
            print(f"Usuário:     {t['usuario']}")
            print(f"Data:        {t['data']}")
            print(f"Status:      {t['status']}")
            print("="*50)
            return t
    
    print(f"\n✗ Ticket #{ticket_id} não encontrado.")
    return None


def fazer_login():
    """
    Realiza autenticação do usuário usando credenciais do config.py.
    
    Returns:
        bool: True se login bem-sucedido, False caso contrário
    """
    print("\n=== LOGIN ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in USUARIOS and USUARIOS.get(usuario) == senha:
        print(f"✓ Login realizado: {usuario}")
        return True
    else:
        print("✗ Usuário ou senha inválidos")
        return False


def main():
    """Função principal que controla o fluxo de execução do sistema"""
    print("\n🎫 Bem-vindo ao SigTicket!")
    
    if not fazer_login():
        print("Acesso negado. Encerrando...")
        return
    
    while True:
        menu_principal()
        
        try:
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                criar_ticket()
            elif opcao == "2":
                listar_tickets()
            elif opcao == "3":
                mudar_status()
            elif opcao == "4":
                try:
                    tid = int(input("\nID do ticket para buscar: "))
                    buscar_ticket(tid)
                except ValueError:
                    print("\n✗ ID inválido!")
            elif opcao == "5":
                print("\nEncerrando sistema... Até logo!")
                break
            else:
                print("\n✗ Opção inválida!")
        
        except KeyboardInterrupt:
            print("\n\nSistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")


def carregar_dados_teste():
    """Carrega tickets de exemplo com problemas intencionais (para testes)"""
    global contador_id
    tickets.extend([
        {
            "id": 1,
            "titulo": "Impressora não funciona",
            "descricao": "A impressora do 3º andar está offline",
            "usuario": "joao.silva",
            "data": "01/12/2025",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Senha esquecida",
            "descricao": "Usuário não consegue acessar o sistema",
            "usuario": "maria.santos",
            "data": "32/13/2025",
            "status": "em analise"
        },
        {
            "id": 3,
            "titulo": "Computador lento",
            "descricao": "Máquina travando constantemente",
            "usuario": "pedro.costa",
            "data": "abc/def/ghij",
            "status": "xpto"
        }
    ])
    contador_id = 4
    print("✓ Dados de teste carregados (3 tickets com problemas)")


if __name__ == "__main__":
    # Descomente para carregar dados de teste
    carregar_dados_teste()
    main()
