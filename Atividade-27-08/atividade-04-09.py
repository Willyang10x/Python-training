codeNutri = 2
contador = 0
soma_salarios = 0.0

while True:
    codigo = int(input("Código do cargo (inteiro): "))
    if codigo <= 0:
        break
    salario = float(input("Salário (use ponto como separador decimal): "))
    if codigo == codeNutri:
        contador += 1
        soma_salarios += salario

print(f"Quantidade de código {codeNutri}: {contador}")
print(f"Soma dos salários para código {codeNutri}: {soma_salarios:.2f}")