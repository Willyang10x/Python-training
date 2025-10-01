"""x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"{distancia:.4f}")"""

"""valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]


for nota in notas:
    quantidade = valor // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    valor = valor % nota"""

"""nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota:"))
nota3 = float(input("Insira sua terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Você foi aprovado e tirou {media:.1f}")
else:
    print(f"Você foi reprovado! com nota {media:.1f}")"""

print("Ola, aproveite a mercadoria e boas compras!")
nome = input("Insira o seu nome:")
idade = int(input("Insira sua idade:"))
if idade >=18:
   print(f"Maior de idade. {idade}")
else:
   print(f"Menor de idade {idade}")
endereco =input("Insira o seu endereco:")
n = int(input("Insira o numero da sua residencia:"))
escolha = input("EScolha seus produtos:")

print(f"nome: {nome}\nidade: {idade}\nendereço:{endereco}\nnumero da rua: {n}\nSeus produtos:{escolha}\nCompras finalizdas! Aproveite sua feira e volte sempre." )
