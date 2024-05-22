menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

:: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if (opcao == "d"):
        print("Deposito")
        
        valor_deposito = float(input("Insira o valor que deseja depositar: "))

        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"+ Depósito no valor de R$ {valor_deposito:.2f}\n"

        else:
            print("""Operação Inválida!
                Não é possível realizar depósitos de valores negativos.
            """)

    elif (opcao == "s"):
        print("Saque")

        if(saldo <= 0):
             print("Você não possui saldo para realizar saque.")

        else:
            valor_saque = float(input("Insira o valor que deseja retirar: "))

            if(saldo < valor_saque):
                print(f""" Você não possui saldo suficente para esta operação. 
                Saldo em conta: R$ {saldo:.2f}
                Valor retirada: R$ {valor_saque:.2f}
                """)

            elif(valor_saque > limite):
                print(f""" Operação Inválida! 
                    O valor limite para saque é de R${limite}.
                    """)

            elif(numero_saques >= LIMITE_SAQUES):
                print(f""" Operação Inválida! 
                    Você já  realizou os {LIMITE_SAQUES} saques permitidos hoje.
                    """)

            elif(valor_saque > 0):
                saldo -= valor_saque
                extrato += f"- Saque no valor de R$ {valor_saque:.2f}\n"
                numero_saques += 1


    elif (opcao == "e"):
        print("\n ------------------- Extrato ------------------- \n")
#        if(extrato == ""):
#            print("\n Não foram realizadas movimentações na conta." if not extrato else extrato)
        print("\n Não foram realizadas movimentações na conta.\n" if not extrato else extrato)
        print(f"\n Saldo em conta: R$ {saldo:.2f}")
        print("\n ----------------------------------------------- \n")

    elif (opcao == "q"):
        print("SAIR")
        exit()

    else:
        print("Opcao invalida.")