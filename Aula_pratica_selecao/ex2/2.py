numero1 = int(input("Digite um número: "))
elevado = int(input("Digite o expoente: "))
controle = 1
numero = numero1
while controle < elevado or controle == 1:
    if elevado == 1:
        print(numero)
        controle += 1
    else:       
        numero *= numero1
        controle += 1
        print(numero)