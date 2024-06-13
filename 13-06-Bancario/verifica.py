import time

def day(mes):
    print("Mês",mes, end="", flush=True)
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)

def deposito(saldo, extrato):
    a = float(input("Digite o seu deposito: R$"))
    if a > 0:
        saldo += a
        extrato += f"\nDeposito: R${saldo:.2f} "
        print(f"Depósito realizado com sucesso! Novo saldo: R${saldo:.2f}")
    else:
        print("O valor de deposito é inválido!")
    return saldo, extrato


def saque(saldo, extrato, limite_valor, contagem):

    b = float(input("Digite o valor que deseja sacar R$"))

    if b > limite_valor:
        print("Valor do saque excede o limite permitido.")
    elif b > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= b
        extrato += f"\nSaque: R${b:.2f} "
        contagem += 1
        print(f"Saque realizado com sucesso! Novo saldo: R${saldo:.2f}")
    return saldo, extrato, contagem


def extrato(extrato, saldo):
    print("----------Extrato----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")