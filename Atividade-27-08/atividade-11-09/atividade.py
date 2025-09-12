"""
numero = input("Insira um numero:")

print(f"O numero informado foi {numero}")

"""

"""
numero1 = int(input("Insira um numero:"))
numero2 = int(input("Insira outro numero:"))

numeros = numero1 + numero2

print(f"A soma dos numero é {numeros}")
"""

"""
nota1 = float(input("Insira sua 1 nota:"))
nota2 = float(input("Insira sua 2 nota:"))
nota3 = float(input("Insira sua 3 nota:"))
nota4 = float(input("Insira sua 4 nota:"))

notas = (nota1+nota2+nota3+nota4)/4

print(f"A sua média é {notas}")
"""

"""
tempCelsius = float(input("Insira uma temperatura em Celsius:"))

tempF = (tempCelsius*9/5) + 32

print(f"A temperatura convertida em fahrenheit é: {tempF}")
"""

"""
tamanho_gb = float(input("Digite o tamanho do arquivo em GBs:"))
tamanho_mb = tamanho_gb * 1_024
tamanho_kb = tamanho_gb * 1_024 * 1_024
print(f"O arquivo tem {tamanho_mb} MBs ou {tamanho_kb} Kbs")
"""
"""
hora_trabalho = float(input("Insira quanto vc ganha por hora:"))
salario = float(input("Insira quantas horas vc trabalhou:"))

inss = hora_trabalho * 0.08
ir = hora_trabalho * 0.11
sindicato = hora_trabalho * 0.05

salario_bruto = hora_trabalho * salario

salatio_liquido = hora_trabalho-inss-ir-sindicato
print(f"O salario bruto é:{salario_bruto}\n menos inss {inss}\n menos ir {ir}\n menos sindicato {sindicato}\n Salario liquido {salatio_liquido}")
"""

"""
numero1 = float(input("Insira um numero:"))
numero2 = float(input("Insira outro numero:"))

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)
"""

"""
nome1 = input("Insira o nome do produto 1: ")
valor1 = float(input(f"Insira o valor do produto '{nome1}': "))

nome2 = input("Insira o nome do produto 2: ")
valor2 = float(input(f"Insira o valor do produto '{nome2}': "))

nome3 = input("Insira o nome do produto 3: ")
valor3 = float(input(f"Insira o valor do produto '{nome3}': "))

if valor1 < valor2 and valor1 < valor3:
    print(f"O produto mais barato é '{nome1}' custando R${valor1:.2f}")
elif valor2 < valor1 and valor2 < valor3:
    print(f"O produto mais barato é '{nome2}' custando R${valor2:.2f}")
else:
    print(f"O produto mais barato é '{nome3}' custando R${valor3:.2f}")
"""

"""
nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota:"))

media = (nota1+nota2)/2

if media > 9 and media <= 10:
    print(f"Sua nota é {media}: A")
if media > 7.5 and media <= 9:
    print(f"Sua nota é {media}: B")
if media > 6 and media <= 7.5:
    print(f"Sua nota é {media}: ")
if media > 4 and media <= 6:
    print(f"Sua nota é {media}: D")
if media > 4 and media <= 0:
    print(f"Sua nota é {media}: E")
"""

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais que 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("A idade deve estar entre 0 e 150.")
    except ValueError:
        print("Digite um número válido para a idade.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("O salário deve ser maior que zero.")
    except ValueError:
        print("Digite um valor numérico para o salário.")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Use: s (solteiro), c (casado), v (viúvo), d (divorciado).")

print("\n✅ Dados validados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Estado Civil: {estado_civil}")