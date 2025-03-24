import random

op = 1
while op == 1:
    print("===================================")
    print("       Bem-vindo ao Jogo!")
    print("===================================")
    print("Tente adivinhar o número secreto!")
    print("O número está entre 1000 e 9999.")
    print("Você terá 10 tentativas por rodada.")
    print("A partir da 5ª tentativa, você receberá dicas.")
    print("Boa sorte!")
    print("===================================\n")
    numero_secreto = random.randint(1000, 9999)
    milhar = numero_secreto // 1000
    centena = (numero_secreto % 1000) // 100
    dezena = (numero_secreto % 100) // 10
    unidade = numero_secreto % 10
    tentativas = 0
    print("\nUma nova rodada começou!")
    while tentativas < 10:
        certos = ""
        tentativa = int(input(f"Tentativa {tentativas + 1}/10: Digite seu palpite: "))
        while tentativa < 1000 or tentativa > 9999:
            tentativa = int(input("Por favor, insira um número entre 1000 e 9999: "))
        tentativas += 1
        milharE = tentativa // 1000
        centenaE = (tentativa % 1000) // 100
        dezenaE = (tentativa % 100) // 10
        unidadeE = tentativa % 10
        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            tentativas = 10
        else:
            print("Errado!")
            if milharE == milhar:
                certos = f"{milhar}"
            else:
                certos = certos + "_"
            if centenaE == centena:
                certos = certos + f"{centena}"
            else:
                certos = certos + "_"
            if dezenaE == dezena:
                certos = certos + f"{dezena}"
            else:
                certos = certos + "_"
            if unidadeE == unidade:
                certos = certos + f"{unidade}"
            else:
                certos = certos + "_"
            print("", certos)
            print()
            if tentativas >= 5:
                if tentativa > numero_secreto:
                    print("Dica: O número secreto é menor!")
                elif tentativa < numero_secreto:
                    print("Dica: O número secreto é maior!")
    if tentativas == 10:
        print(f"O número secreto era {numero_secreto}.")
    op = int(input("Deseja jogar novamente? (1 - Sim, 0 - Não): "))