"""
numero = int(input("Insira um número:"))

if numero % 2 == 0:
    print(f"Seu numero positivo e o resultado é: {numero**2}")
else:
    print(f"Seu numero é negativo e o resultado é: {numero**3}")
"""
"""
opcao = int(input("Digite o número da opção que você quer: "))

if opcao == 1:
    bit1 = int(input("Digite um bit (0 ou 1): "))
    bit2 = int(input("Digite um bit (0 ou 1): "))
    if bit1 not in [0, 1] or bit2 not in [0, 1]:
        print("Digite apenas bits (0 ou 1).")
        exit()
    resultado = bit1 & bit2
    print(f"{bit1} AND {bit2} = {resultado}")

elif opcao == 2:
    bit1 = int(input("Digite um bit (0 ou 1): "))
    bit2 = int(input("Digite um bit (0 ou 1): "))
    if bit1 not in [0, 1] or bit2 not in [0, 1]:
        print("Digite apenas bits (0 ou 1).")
        exit()
    resultado = bit1 | bit2
    print(f"{bit1} OR {bit2} = {resultado}")

elif opcao == 3:
    bit1 = int(input("Digite um bit (0 ou 1): "))
    if bit1 not in [0, 1]:
        print("Digite apenas bits (0 ou 1).")
        exit()
    print(f"NOT {bit1} = {1 - bit1}")

else:
    print("Opção inválida, tente novamente!")
"""

"""
usuario = input("Digite seu Usuário: ")
senha = input("Digite sua senha: ")

if usuario == "procopio" and senha == "12345":
    print(f"Seja bem-vindo")
elif usuario == "paiva" and senha == "54321":
    print(f"Seja bem-vindo")
else:
    print("Usuário e senha não conferem")
"""

"""
salario = float(input("Digite o valor do seu salário: "))
cargo = int(input("********CARGOS********\n\n1. Programador de sistemas\n2. Analista de Sistemas\n3. Analista de Banco de Dados\n\nDigite o número do seu cargo: "))

if cargo == 1:
   aumento = salario * 30/100
   salario_com_aumento = salario + aumento
   print(f"Seu salário com aumento de 30%: {salario_com_aumento}")
elif cargo == 2:
   aumento = salario * 20/100
   salario_com_aumento = salario + aumento
   print(f"Seu salário com aumento de 20%: {salario_com_aumento}")
elif cargo == 3:
    aumento= salario * 15/100
    salario_com_aumento = salario + aumento
    print(f"Seu salário com aumento de 15%: {salario_com_aumento}")
else:
    print("Cargo inválido!")

"""

"""
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/altura**2

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25.0:
    print("Peso normal")
elif imc >= 25.0 and imc < 30.0:
    print("Sobrepeso")
elif imc >= 30.0 and imc < 35.0:
    print("Obesidade grau 1")
elif imc >= 35.0 and imc < 40.0:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

"""