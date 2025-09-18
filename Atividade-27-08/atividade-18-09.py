"""import math

quantidade = int(input("Digite a quantidade de números da lista: "))
L = []

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º número: "))
    L.append(valor)

print(f"Lista L: {L}")

menor = L[0]
for numero in L:
    if numero < menor:
        menor = numero
maior = L[0]
for numero in L:
    if numero > maior:
        maior = numero

print(f"Menor elemento: {menor}")
print(f"Maior elemento: {maior}")

media_geom = math.sqrt(menor * maior)

print(f"Média geométrica entre {menor} e {maior} = {media_geom:.2f}")"""
