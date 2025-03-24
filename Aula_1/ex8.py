premio = float(input("Informe o valor do premio: "))

primeiro = premio * (46/100)
segundo = premio * (32/100)
terceiro = premio - (primeiro + segundo)

print("O primeiro receberá: ", primeiro, " reais")
print("O segundo receberá: ", segundo, " reais")
print("O terceiro receberá: ", terceiro, " reais")