import random

secreto = random.randint(1, 10)
tentativas = 0

print("🎲 Adivinhe o número entre 1 e 10!")

while True:
    chute = int(input("Seu palpite: "))
    tentativas += 1

    if chute == secreto:
        print(f"Acertou! O número era {secreto}. Tentativas: {tentativas}")
        break
    elif chute < secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")