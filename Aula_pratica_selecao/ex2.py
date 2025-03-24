numero1 = int(input("Digite um número: "))
elevado = int(input("Digite o expoente: "))
numero = numero1
for i in range(0, elevado):
    numero *= numero1
    print(numero)