"""disciplinas = {"Magna":"Python","Andre":"ICL"}
disciplinas.update({"Auricelio":"Ingles"})
print(disciplinas)"""


"""produtos = {
    1: {"nome": "Monitor LED 24", "preco_unitario": 599.99, "quantidade": 1},
    2: {"nome": "Teclado wireless", "preco_unitario": 49.26, "quantidade": 1},
    3: {"nome": "Mouse wireless", "preco_unitario": 19.90, "quantidade": 1},
    4: {"nome": "Cartucho colorido", "preco_unitario": 54.00, "quantidade": 2}
}

total = 0

print("Itens da compra:\n")

for codigo, dados in produtos.items():
    subtotal = dados["preco_unitario"] * dados["quantidade"]
    print(f"{dados['nome']} - Qtde: {dados['quantidade']} - Preço: R$ {dados['preco_unitario']:.2f} - Subtotal: R$ {subtotal:.2f}")
    total += subtotal

print("\nValor total da compra: R$ {:.2f}".format(total))"""

"""carro = {
    1: {"marca":"ford","modelo": "ka","ano":2005},
    2: {"marca":"fiat","modelo": "uno","ano":2008}
}

print(carro)"""

"""aluno = {"matricula":157,"nome": "kaka","telefone":80028922, "curso":"Ads"}

print(aluno["matricula"])"""

"""caderno = {"Gabriel":6999999,"denis":5454545,"Barry":12456778}

print(caderno["Gabriel"])"""

"""instagram = {"@bl77":"lucasb","@gbl777":"bielzão"}

print(instagram["@gbl777"])"""

"""contatos = {"@ana":"Ana","@joao":"joao"}
print(contatos.get("@maria"))

não tem na lista retorna "none".
"""

"""estoque = {
    "Mouse":1,
    "Teclado":4

}

estoque.update({"HUB USB":3})
estoque.update({"Teclado":1})

print(estoque)"""

"""cidades = {
    "São Paulo":"SP",
    "Areial":"PB",
    "Santa Catarina": "SC",
    "João Pessoa": "PB"
}

print(len(cidades))"""

"""agenda = {"Carlos":"04904445","Elsisa":"442444"}

if "Carlo" in agenda:
    print(f"{agenda} Ele está na agenda!")
else:
    print(f"Não encontrado!")"""

"""notas = {"Artes":10,"Português":7,"Inglês":5}

print(notas.keys())
print(notas.values())"""

"""livros = {
    "pequeno":"Denys",
    "principe":"paraiba",
    "Harry":"Potter"
          
}
for titulo, autor in livros.items():
    print(f"Titulo: {titulo}\nAutor: {autor}")"""