n = int(input("Informe a quantidade de números desejada: "))
somapar = 0
qnttimpar = 0
for x in range(n):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        somapar += numero
    else:
        qnttimpar += 1

print("Quantidade de ímpares: ", qnttimpar)
print("Soma dos pares: ", somapar)