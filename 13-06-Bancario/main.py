#--Main--
import verifica

print("Programa Bancário")
print()

limite_saque = 3
contagens_saques = 0
limite_valor_saque = 500.00
extrato = ""
saldo = 0
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
menu = ["d", "s", "e"]


for j in range(12):
    verifica.day(mes[j])
    print("")

    print()
    opcao = input(f"Bem-Vindo o que deseje fazer em seu banco? {menu}").lower()
    print()

    if opcao in menu:
        if opcao == "d":
            saldo, extrato = verifica.deposito(saldo, extrato)

        elif opcao == "s":
            if contagens_saques < limite_saque:
               saldo, extrato, contagem_saques = verifica.saque(saldo, extrato, limite_valor_saque, contagens_saques)
            else:
                print("Limite diário de saques atingido.")

        elif opcao == "e":
            verifica.extrato(extrato, saldo)

        else:
            print("Operação inválida!")
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")