a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
if a + b < c:
    print(f"A soma de a + b é igual a {a + b} e é menor que c")
elif a + b > c:
    print(f"A soma de a + b é igual a {a + b} e é maior que c")
else:
    print(f"A soma de a + b é igual a {a + b} e é igual a c")