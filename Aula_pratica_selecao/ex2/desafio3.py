numero = int(input("Digite um número: "))
contador = 1
numero1 = numero
while contador < numero:
    numero1 *= (numero - contador)
    print(numero1)
    contador += 1