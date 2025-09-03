quantidade_numeros = int(input("Digite a quantidade de números que você deseja inserir: "))
contador = 0
soma = 0  # variável para acumular os valores

while contador < quantidade_numeros:
    valor = int(input("Digite o valor para calcular a média: "))
    soma += valor
    contador += 1

media = soma / quantidade_numeros
print(f"A média dos números digitados é: {media}")