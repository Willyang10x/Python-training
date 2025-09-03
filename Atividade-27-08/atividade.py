termo = int(input("Digite o número de termos: "))
quantidade_termo = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))
ultimo_termo = termo + (quantidade_termo - 1) * razao
for i in range(termo, ultimo_termo + 1, razao):
    print(i, end=" ")
