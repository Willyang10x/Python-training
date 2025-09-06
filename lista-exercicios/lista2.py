"""
altura = float(input("Insira sua altura:"))

centimetros = altura * 100

print(f"Sua altura foi convertida em Centrimetros: {centimetros}")

"""

"""
deslocamento = float(input("Insira o deslocamento do objeto em metros:"))

variacaoTempoSegundo = 60

velocidadeMedia = deslocamento / variacaoTempoSegundo

print(f"A velocidade media em segundos do objeto é: {velocidadeMedia} segundos.")

"""

"""
valor = float(input("Insira um valor:"))
pi = 3.1415
area  = pi* (valor ** 2)

print(area)

"""

"""
base = float(input("Insira o valor da base:"))
altura = float(input("Insira a altura:"))

areaTriangulo = (base*altura) / 2

print(areaTriangulo)
"""
"""
numero1 = int(input("Insira um número:"))
numero2 = int(input("Insira outro número:"))

print(f"A soma dos números é: {numero1+numero2}\nE o produto entre eles é: {numero1*numero2}")

"""
"""
copo1 = "laranja"
copo2 = "acerola"

copo1,copo2 = copo2,copo1

print(f"copo 1 {copo1}\ncopo 2 {copo2}")

"""
"""
precoCamisa = 12.50

valor = int(input("Insira quantas camisas vai querer?"))

total_sem_desconto = precoCamisa * valor

if valor <= 5:
    desconto = 0.03 
elif valor <= 10:
    desconto = 0.05 
else: 
    desconto = 0.07 

valor_desconto = total_sem_desconto * desconto
total_com_desconto = total_sem_desconto - valor_desconto

print(f"O valor total das camisas é R$ {total_com_desconto:.2f}")

"""
"""
def ordenar_estaturas():
  
  estaturas = []
  for i in range(3):
    estatura = float(input(f"Digite a estatura da pessoa {i + 1} (em metros): "))
    estaturas.append(estatura)

  estaturas.sort(reverse=True)
  
  print("\nEstaturas em ordem decrescente:")
  for estatura in estaturas:
    print(f"{estatura} m")

ordenar_estaturas()
"""
"""
numero = int(input("Digite um número inteiro positivo: "))

if numero % 2 == 0:
  resultado = numero ** 2
else:
  resultado = numero ** 3

print(f"O resultado é: {resultado}")
"""
"""
n1 = float(input("Digite o primeiro número positivo: "))
n2 = float(input("Digite o segundo número positivo: "))

print("\nEscolha uma opção:")
print("1. Média ponderada (pesos 2 e 3)")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")

opcao = input("Digite o número da opção desejada: ")

if opcao == '1':
  resultado = (n1 * 2 + n2 * 3) / 5
  print(f"A média ponderada é: {resultado}")
elif opcao == '2':
  resultado = (n1 + n2) ** 2
  print(f"O quadrado da soma é: {resultado}")
elif opcao == '3':
  if n1 < n2:
    menor = n1
  else:
    menor = n2
  resultado = menor ** 3
  print(f"O cubo do menor número é: {resultado}")
else:
  print("Opção inválida")
"""