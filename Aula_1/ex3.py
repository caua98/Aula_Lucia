salario = float(input("Informe seu salário: "))
percentual = float(input("Informe a porcentagem de reajuste: "))
valor = 0
op = input("Será Deduzido esse valor ou Somado?(D/S): ")

if op == "D":
    valor = salario * (percentual/100)
    salario = salario - valor
    print("Seu novo salário é: ", salario)

if op == "S":
     valor = salario * (percentual/100)
     salario = salario + valor
     print("Seu novo salário é: ", salario)
