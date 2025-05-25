menu = """

[0] DEPOSITAR
[1] SACAR
[2] EXTRATO
[3] SAIR

-> """

saldo = 0 #Valor inicial da conta
limite = 500 #limite de saque por tentativa
extrato = "" 
numero_saques = 0 #quantidade de saques efetivado
LIMITE_SAQUES = 3 #quantidade de saques disponivel 


while True:
    opcao = input(menu)
    
# Depositar apenas valores positivos
# Armazenar os depositos em uma variavel e exibilos na operação de extrato

    if opcao == "0":
        print("Você selecionou a opção [0] = DEPOSITAR")
        
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("A operação não pode ser concluída! O valor digitado é invalido.")

# 3 saques diarios
# saque maximo de R$ 500.00
# valor > saldo = exibir mensagem informando que o saldo não é suficiente
# todos os saques devem ser armazenados na variavel extrato

    elif opcao == "1":
        print("Você selecionou a opção [1] = SACAR")

        valor = float(input("Informe o valor que deseja sacar: "))

        sem_saque_diario = numero_saques >= LIMITE_SAQUES

        excedeu_limite_saque = valor > limite

        saldo_insuficiente = valor > saldo


        if sem_saque_diario:
            print("Operação não pode ser concluída! Você atingiu o limite de saque diário.")

        elif excedeu_limite_saque:
            print("Operação não pode ser concluída! O valor de saque excede o limite de saque.")

        elif saldo_insuficiente:
            print("Operação não pode ser concluída! Saldo insuficiente.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não pode ser concluída! Valor informado inválido.")


# armazena todos os depositos e saues realizados
# exibir o saldo atual ao fim da listagem
# formatação R$ xxx.xx

    elif opcao == "2":
        print("Você selecionou a opção [2] =  EXTRATO")

        print("\n==========EXTRATO==========")
        print(f"Movimentações realizadas: \n{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===========================")

    elif opcao == "3":
        break

    else:
        print("Opção inválida! Tente uma das opção abaixo: ")
