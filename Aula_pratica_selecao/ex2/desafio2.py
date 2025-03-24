controle = 0
maior = 0
while controle < 3:
    numero1 = int(input("Digite um número: "))
    if numero1 > maior:
        maior = numero1
    controle += 1

print(f"O maior número digitado foi {maior}")