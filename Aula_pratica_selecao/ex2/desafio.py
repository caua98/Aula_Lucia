nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
peso1 = float(input("Informe o peso da primeira nota: "))
peso2 = float(input("Informe o peso da segunda nota: "))

valor1 = nota1 * peso1
valor2 = nota2 * peso2
media = (valor1 + valor2) / (peso1 + peso2)
if media <= 7:
    print("Reprovado")
elif media > 7 and media < 10:
    print("Aprovado") 
elif media == 10: 
    print("Aprovado com distinção")