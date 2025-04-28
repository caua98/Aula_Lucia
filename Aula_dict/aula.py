dicionario = {}
for a in range(10):
    nome = input("Digite seu nome: ")
    idade = input("Informe sua idade: ")
    cidade = input("Informe sua cidade: ")
    if nome in dicionario.keys():
        valor_retirado = dicionario.pop(nome)
        dicionario[nome] = [idade, cidade]
        print(dicionario[nome])
        print(valor_retirado)
    else:
        dicionario[nome] = [idade, cidade]

print(dicionario)