saldo = 10000

opcao = int(input("Informe um opcao: [1] Saque, [2] Depósito, [3]Saldo: "))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        print(f"Saque realizado com sucesso. Saldo atual: {saldo:.2f}")
elif opcao == 2:
    valor = float(input("Informe o valor do depósito: "))
    saldo += valor
    print(f"Depósito realizado com sucesso. Saldo atual: {saldo:.2f}")
elif opcao == 3:
    print(f"Saldo atual: {saldo:.2f}")
else:
    print("Opção inválida")