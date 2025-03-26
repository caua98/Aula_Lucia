numero = (int(input("Digite um número: ")))
S = 0
for a in range(1, numero + 1):
    S += 2*(a - 1) + (a - 1)
    print(S, a)