"""
lista = ["Carolina", 1.70, 19]
lista.append("Ana")

print(f"Nome: {lista[0]}")
print(f"Altura: {lista[1]}")
print(f"Idade: {lista[2]}")
print(f"Nome: {lista[3]}")
"""

"""
atrizes = ["Paolão"]
atrizes.append("Gabriel")

while True:
    nome = input("Digite seu nome:")
    atrizes.append(nome)
    resp = input("deseja continuar [S,N]?")
    if resp.upper() == "N":
        break
print(atrizes)
"""

"""
import random

atrizes = ["Ana", "Julia", "juca"]
random.shuffle(atrizes)
print(f"Lista embaralhada: {atrizes}")
sorteada = random.choice(atrizes)
print(f"Atriz sorteada: {sorteada}")
"""

"""
atrizes = ["Ana", "Julia", "juca"]
atrizes.pop(0)
atrizes.insert(0,"Ana julia")
del atrizes [2]

print(atrizes)
"""

"""
nomes = []
tempos = []

for i in range(7):
    nome = input(f"Digite o nome do {i+1}º nadador: ")
    tempo = float(input(f"Digite o tempo do {i+1}º nadador (em segundos): "))
    
    nomes.append(nome)
    tempos.append(tempo)

melhor_tempo = min(tempos)
indice_melhor = tempos.index(melhor_tempo)
melhor_nadador = nomes[indice_melhor]


pior_tempo = max(tempos)
indice_pior = tempos.index(pior_tempo)
pior_nadador = nomes[indice_pior]

media = sum(tempos) / len(tempos)


print("\n===== RELATÓRIO =====")
print(f"Nadador com melhor tempo: {melhor_nadador} ({melhor_tempo:.2f} s)")
print(f"Nadador com pior tempo: {pior_nadador} ({pior_tempo:.2f} s)")
print(f"Tempo médio dos nadadores: {media:.2f} s")
"""

