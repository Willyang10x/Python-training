"""1) Para que serve a função range?
Gerar sequências numéricas sob demanda, otimizando o uso de memória."""

"""2) As listas são mutáveis e podem conter diferentes tipos de dados"""

"""3) O range em Python é uma função flexível, que aceita até três argumentos: o fim (stop),
início (start) e pulo (step) da sequência. Dessa forma, conseguimos ajustar o
comportamento da sequência numérica gerada, de acordo com a necessidade."""

# Repetindo uma frase 5 vezes
"""for i in range(5):
    print("Hello Word!")"""

# Como usar range len em Python
"""cores = ['vermelho', 'azul', 'verde']
for i in range(len(cores)):
    cor = cores[i]
    print(f'Cor no índice {i} é: {cor}')"""

# função enumerate nestes casos, que já retorna cada elemento juntamente de seu índice em um loop
"""cores = ['vermelho', 'azul', 'verde']
for i, cor in enumerate(cores):
    print(f"Cor no indice {i+1} é: {cor}")"""