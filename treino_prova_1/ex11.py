salario = float(input("Informe seu salário: "))
qntt = 0 
maior = 0
filhos = 0
qnttM = 0
soma = 0
while salario >= 0:
    filhos += int(input("Informe a qntt de filhos: "))
    qntt += 1
    if maior < salario:
        maior = salario
    if salario < 1500:
        qnttM += 1
    soma += salario
    salario = float(input("Inofrme outro salário: "))

print(f"A porcentagem de pessoas com salário menor que 1500 é {(qnttM*100)/qntt: .2f}")
print(f"A média de filhos é {filhos/qntt: .2f}")
print(f"A média de salário é {soma/qntt: .2f}")
print(f"O maior salário é {maior}")