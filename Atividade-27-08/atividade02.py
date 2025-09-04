total = 0.0
mais_barato_nome = ""
mais_barato_preco = float("inf")

for i in range(0, 5):
    nome = input(f"Nome do medicamento {i}: ").strip()
    preco_str = input(f"Preço do medicamento {i} (R$): ").strip()
    preco = float(preco_str.replace(",", "."))  # aceita vírgula ou ponto

    total += preco
    if preco < mais_barato_preco:
        mais_barato_preco = preco
        mais_barato_nome = nome

media = total / 5

print("\nResultados:")
print(f"Mais barato: {mais_barato_nome} — R$ {mais_barato_preco:.2f}")
print(f"Média dos preços: R$ {media:.2f}")