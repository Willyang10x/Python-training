"""from operator import itemgetter

relatorio = {"Betano":100000,"Betb":80000}

for empresa, valor in sorted(relatorio.items(),key=itemgetter(0)):
    print(f"{empresa} -> {valor}")"""


"""turma = {}

while True:
    nome = input("Nome do aluno (ou ENTER para parar): ")
    if nome == "":
        break
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso / (altura**2)

    turma[nome] = {
        "altura" : altura,
        "peso" : peso,
        "imc" : imc
    }

print("\nAlunos e seus IMCs: ")
for nome in sorted (turma.keys()):
    print(f"{nome}: {turma[nome]["imc"]:.2f}")"""



"""voos = {}

while True:
    numero = input("Número do voo (ou ENTER para parar): ")
    if numero == "":
        break
    origem = input("Origem: ")
    destino = input("Destino: ")
    voos[numero] = {"origem": origem, "destino": destino}

qtd = sum(1 for v in voos.values() if v["destino"].lower() == "natal")
print(f"\nQuantidade de voos com origem Natal: {qtd}")"""

"""voos = {}

while True:
    numero = input("Número do voo (ou ENTER para parar): ")
    if numero == "":
        break
    origem = input("Origem: ")
    destino = input("Destino: ")
    voos[numero] = {"origem": origem, "destino": destino}
voos = {num: dados for num, dados in voos.items() if dados["destino"].lower() != "recife"}

print("\nVoos após remoção de destino Recife:")
for num, dados in voos.items():
    print(f"Voo {num}: {dados['origem']} -> {dados['destino']}")"""

"""voos = {}

while True:
    numero = input("Número do voo (ou ENTER para parar): ")
    if numero == "":
        break
    origem = input("Origem: ")
    destino = input("Destino: ")
    voos[numero] = {"origem": origem, "destino": destino}

print(f"{voos}")

num = input("Digite o número do voo que deseja alterar: ")
if num in voos:
    nova_origem = input("Nova origem (ENTER para não alterar): ")
    novo_destino = input("Novo destino (ENTER para não alterar): ")
    if nova_origem:
        voos[num]["origem"] = nova_origem
    if novo_destino:
        voos[num]["destino"] = novo_destino
else:
    print("Voo não encontrado.")

print("\nVoos atualizados:")
for num, dados in voos.items():
    print(f"Voo {num}: {dados['origem']} -> {dados['destino']}")"""


"""series = {}

while True:
    titulo = input("Título da série (ou ENTER para parar): ")
    if titulo == "":
        break
    ator1 = input("Ator principal 1: ")
    ator2 = input("Ator principal 2: ")
    series[titulo] = [ator1, ator2]

for titulo in sorted(series.keys()):
    atores = ", ".join(series[titulo])
    print(f"{titulo}: {atores}")"""