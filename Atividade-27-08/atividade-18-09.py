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


"""
atrizes = ["Ana", "Julia", "juca"]
copia = list(atrizes)

print(copia)
print(atrizes)
"""

"""atrizes = ["Ana", "Julia", "juca"]
backup = list(atrizes)

if backup == list(atrizes):
    atrizes.clear()
    print("Lista de artrizes esvaziada!")
else:
    print("ERRO: Copia gerada não é igual à original.")"""

"""atrizes = ["Ana", "Julia", "juca"]
atrizes_defora = ["joao", "zezo", "lucas"]

atrizes.extend(atrizes_defora)
print(atrizes)"""

"""nome = input("Insira um nome: ")

atrizes = ["Ana", "Julia", "juca"]

ocorrencias = atrizes.count(nome)
print(f"O elemento {nome} se repete {ocorrencias} vezes.")"""

"""atrizes = ["Ana", "Julia", "juca"]
contar = len(atrizes)

print(f"A lista atrizes tem {contar} elementos.")"""

"""notas_turma = [9,5,6,3,1]

menor = min(notas_turma)
maior = max(notas_turma)
soma = sum(notas_turma)/ len(notas_turma)

print(f"O menor numero da lista é {menor}\nO maior numero da lista é {maior}\nA soma das notas da lista é {soma}")"""

"""atrizes = ["Ana", "Julia", "juca"]
procurar_por = "Julia"

if procurar_por in atrizes:
    indice = atrizes.index(procurar_por)
    print(f"{procurar_por} está no indice {indice+1}")
else:
    print(f"{procurar_por} não está na lista")"""


"""atrizes = ["Ana", "Julia", "juca"]
for atrizes in atrizes:
    print(atrizes)"""

"""atrizes = ["Ana", "Julia", "juca"]

for index, nome in enumerate(atrizes):
    print(f"{nome} está armazenado no indice {index+1}")"""


"""primeiro = float(input("Digite o primeiro número da PA: "))
razao = float(input("Digite a razão (o quanto aumenta): "))
quantidade = int(input("Quantos números você quer ver? "))

if quantidade <= 0:
    print("A quantidade deve ser maior que zero!")
else:
    print("Os termos da PA são:")

    termo_atual = primeiro
    soma = 0

    for i in range(quantidade):
        print(f"[{termo_atual}] ", end="")
        soma += termo_atual
        termo_atual += razao
    
    print(f"\n\nA soma dos termos é: {soma}")"""

"""import random

nomeRifa = ["Ana", "Julia", "juca"]
random.shuffle(nomeRifa)
print(f"Lista embaralhada: {nomeRifa}")
sorteada = random.choice(nomeRifa)
print(f"Voce foi sorteada: {sorteada}")"""