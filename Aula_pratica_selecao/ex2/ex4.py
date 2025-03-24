op = "S"
soma = 0
cntt = 0
while op == "S":
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
    elif n % 2 != 0:
        cntt += 1
    op = input("Deseja continuar?(S/N): ")

print(f"A soma dos números pares é {soma}")
print(f"A quantidade de números ímpares é {cntt}")