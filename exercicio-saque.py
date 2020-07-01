saldo = 0
valor_saque = float(input("Digite o valor de saque: "))

if valor_saque > saldo:
    print("Impossível realizar essa ação.")
else:
    saldo = saldo - valor_saque
    print("Seu novo saldo é de: ", saldo)

