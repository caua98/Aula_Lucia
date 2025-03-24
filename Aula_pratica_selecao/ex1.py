salario = float(input("Informe o salário: "))
plano = input("Informe o plano de aumento: ")

if plano == '1':
    salario += salario * 0.1
    print(f"O salário com aumento é de R${salario:.2f}")
elif plano == '2':
    salario += salario * 0.2
    print(f"O salário com aumento é de R${salario:.2f}")
elif plano == '3':
    salario += salario * 0.3
    print(f"O salário com aumento é de R${salario:.2f}")
else:
    print("Plano inválido")