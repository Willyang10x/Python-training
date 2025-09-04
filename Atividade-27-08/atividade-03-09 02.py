homens_maior_18 = 0
mulheres = 0

while True:
    idade = int(input("Digite a idade do aluno (negativa para encerrar): "))
    
    if idade < 0:
        break
    
    sexo = input("Digite o sexo do aluno (M/F): ").strip().upper()
    
    if sexo == "M" and idade > 18:
        homens_maior_18 += 1
    elif sexo == "F":
        mulheres += 1

print(f"Quantidade de homens acima de 18 anos: {homens_maior_18}")
print(f"Quantidade de mulheres de qualquer idade: {mulheres}")