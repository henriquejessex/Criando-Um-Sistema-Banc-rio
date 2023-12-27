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

def criar_usuario(usuarios):
    cpf = input("Informe o CPF ( somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ CPF já cadastrado. @@@\n")
        return
        
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço( logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    
    print("\n=== Usuário cadastrado com sucesso! ===\n")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        
def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF ( somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Conta criada com sucesso. @@@\n")
        return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}
    
    print("\n=== Usuario não encontrado! ===\n")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    
    LIMITE_SAQUE = 5
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 0
    usuarios = []
    contas = []
    # Programa principal
    print("\n\n\t\t== Bem-vindo(a) ao Banco do Pobre! ==")

    while True:
        
        opcao = menu()
        
        if opcao == "d":
            print("== Depositar ==")
            valor = float(input("Digite o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            print("== Sacar ==")
            valor = float(input("Digite o valor do saque: "))
            saldo -= valor
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "q":
            print("== Sair ==")
            break # Sai do while True
        
        elif opcao == "nu":
            print("== Novo usuário ==")
            criar_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
        elif opcao == 'lc':
            listar_contas(contas)
            
        else:
            print("== Opcao invalida, por favor selecione novamente. ==")     
        
main()
