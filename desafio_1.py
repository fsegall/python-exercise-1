menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[p] Poupança
[r] Resgatar
[q] Sair

=> """

saldo = 0
poupanca = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "p":
        valor = float(
            input("Informe o valor que deseja transferir para a conta poupança: ")
        )

        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente na conta corrente.")

        elif valor > 0:
            saldo -= valor
            poupanca += valor
            extrato += f"Transferência para Poupança: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "r":
        valor = float(input("Informe o valor que deseja resgatar da conta poupança: "))

        excedeu_saldo = valor > poupanca

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente na conta poupança.")

        elif valor > 0:
            saldo += valor
            poupanca -= valor
            extrato += f"Resgate para Conta Corrente: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nSaldo da Conta Poupança: R$ {poupanca:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
