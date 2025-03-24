a = 1
b = 1
c = 1
d = 1

while a != 0 or b != 0 or c != 0 or d != 0:
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    d = int(input("Digite o valor de d: "))
    e = int(input("Digite o valor de e: "))
    f = int(input("Digite o valor de f: "))
    if (c*e - b*f) == 0 or (a*e - b*d) == 0:
        print("Não é possível calcular")
    else:
        x = (c * e - b * f) / (a * e - b * d)
        print("O valor de x é: ", x)
    if (a*f - c*d) == 0 or (a*e - b*d) == 0:
        print("Não é possível calcular")
    else:
        y = (a * f - c * d) / (a * e - b * d)
        print("O valor de y é: ", y)
