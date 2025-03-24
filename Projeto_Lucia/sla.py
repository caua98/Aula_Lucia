import random

print("===================================")
print("       Bem-vindo ao Jogo!")
print("===================================")
print("Tente adivinhar o número secreto!")
print("O número está entre 1000 e 9999.")
print("Você terá 10 tentativas por rodada.")
print("A partir da 5ª tentativa, você receberá dicas.")
print("Boa sorte!")
print("===================================\n")

jogar_novamente = 1

while jogar_novamente == 1:
    numero_secreto = random.randint(1000, 9999)
    tentativas = 0
    print("\nUma nova rodada começou!")

    for tentativa_atual in range(1, 11):
        tentativa = int(input(f"Tentativa {tentativa_atual}/10: Digite seu palpite: "))

        if tentativa < 1000 or tentativa > 9999:
            print("Por favor, insira um número entre 1000 e 9999.")
            continue

        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            tentativa_atual = 10
        else:
            print("Errado!")

            # Mostrar quais dígitos estão corretos
            temp_tentativa = tentativa
            temp_secreto = numero_secreto
            posicao = 4  # Número de dígitos (4 no caso de 1000 a 9999)

            print("Dígitos corretos nas posições corretas: ", end="")
            while posicao > 0:
                digito_tentativa = temp_tentativa % 10
                digito_secreto = temp_secreto % 10

                if digito_tentativa == digito_secreto:
                    print(digito_tentativa, end=" ")
                else:
                    print("_", end=" ")

                temp_tentativa //= 10
                temp_secreto //= 10
                posicao -= 1
            print()

            if tentativa_atual >= 5:
                diferenca = numero_secreto - tentativa
                if tentativa > numero_secreto:
                    print("Dica: O número secreto é menor!")
                elif tentativa < numero_secreto:
                    print("Dica: O número secreto é maior!")
                if abs(diferenca) <= 10:
                    print("Dica extra: Você está muito perto! A diferença é de no máximo 10.")
                elif abs(diferenca) <= 50:
                    print("Dica extra: Você está perto! A diferença é de no máximo 50.")
                elif abs(diferenca) <= 100:
                    print("Dica extra: Você está relativamente perto! A diferença é de no máximo 100.")

    if tentativa != numero_secreto:
        print(f"Você perdeu! O número secreto era {numero_secreto}.")

    jogar_novamente = int(input("Deseja jogar novamente? (S = 1/N = 0): "))

print("Obrigado por jogar! Até a próxima!")