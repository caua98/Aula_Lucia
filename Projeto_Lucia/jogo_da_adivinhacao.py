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
    controlemilhar = 0
    controlecentena = 0
    controledezena = 0
    controleunidade = 0
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
            if milharE == milhar and controlemilhar == 0:
               controlemilhar = 1
            if centenaE == centena and controlecentena == 0:
                controlecentena = 1
            if dezenaE == dezena and controledezena == 0:
                controledezena = 1
            if unidadeE == unidade and controleunidade == 0:
                controleunidade = 1
            if controlemilhar == 1:
                certos += f'{milhar}'
            else:
                certos += "_"
            if controlecentena == 1:
                certos += f'{centena}'
            else:
                certos += "_"
            if controledezena == 1:
                certos += f'{dezena}'
            else:
                certos += "_"
            if controleunidade == 1:
                certos += f'{unidade}'
            else:
                certos += "_"
            print("", certos)
            print()
            if tentativas >= 5:
                if centena % 2 == 0 and controlecentena == 0:
                    print("Dica: O segundo dígito (centena) é par!")
                elif centena % 2 != 0 and controlecentena == 0:
                    print("Dica: O segundo dígito (centena) é ímpar!")
                elif dezena % 2 == 0 and controledezena == 0:
                    print("Dica: O terceiro dígito (dezena) é par!")
                elif dezena % 2 != 0 and controledezena == 0:
                    print("Dica: O terceiro dígito (dezena) é ímpar!")
                
                
    if tentativas == 10 and tentativa != numero_secreto:
        print("Você não conseguiu adivinhar o número secreto.")
        print(f"O número secreto era {numero_secreto}.")
    print("===================================")
    op = int(input("Deseja jogar novamente? (1 - Sim, 0 - Não): "))