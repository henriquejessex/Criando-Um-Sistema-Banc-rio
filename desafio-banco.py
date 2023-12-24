import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
  
  
def depositar(saldo, valor, extrato, /): # passando parametros posicionais
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: {valor:.2f}\n"        
        print("\n=== Operação realizada com sucesso! ===\n")
    else:
        print("\n@@@Operação falhou! Valor inválido.@@@\n")  
        
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques ): # passando parametros nomeados   
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! Limite excedido. @@@")
    elif excedeu_saque:
        print("\n@@@ Operação falhou! Limite de saques excedido. @@@")
            
            #onde o saque acontece
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    
def exibir_extrato(saldo, /, *, extrato):
        print("\n== Extrato ==")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("================================")
    
# Programa principal
print("== Bem-vindo(a) ao Banco do Pobre! ==")
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 5

while True:
    opcao = menu()
    
    if opcao == "d":
        print("== Depositar ==")
        valor = float(input("Digite o valor do depósito: "))
        
        saldo, extrato = depositar(saldo, valor, extrato)
        
        
    elif opcao == "s":
        print("== Sacar ==")
        valor = float(input("Digite o valor do saque: "))
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "s":
        print("== Sair ==")
        break # Sai do while True
    
    else:
        print("== Opcao invalida, por favor selecione novamente. ==")     
    