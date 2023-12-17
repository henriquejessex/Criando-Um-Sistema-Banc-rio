menu = """
    [D] Depositar
    [S] Sacar
    [T] Transferir
    [E] Extrato
    [S] Sair
    
    
    => Escolha uma opcao: """
    
    
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 5

while True:
    opcao = input(menu).upper() 
    
    if opcao == "D":
        print("== Depositar ==")
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
        
        else:
            print("Operação falhou! Valor inválido")
        
        
    elif opcao == "S":
        print("== Sacar ==")
        valor = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")
        elif excedeu_limite:
            print("Operação falhou! Limite excedido")
        elif excedeu_saque:
            print("Operação falhou! Limite de saques excedido")
            
            #onde o saque acontece
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Valor inválido")
        
    elif opcao == "T":
        print("== Transferir ==")
        
    elif opcao == "E":
        print("\n== Extrato ==")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("================================")
        
    elif opcao == "S":
        print("== Sair ==")
        break # Sai do while True
    
    else:
        print("== Opcao invalida, por favor selecione novamente. ==")     
    