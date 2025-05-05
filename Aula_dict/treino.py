livros = {}
op = "S"
while op == "S":
    print("Digite o código do livro:")
    codigo = input()
    print("Digite o nome do livro:")
    nome = input()
    print("Número de autores:")
    num_autores = int(input())
    autores = []
    for a in range(num_autores):
        print("Digite o nome do autor:")
        autores.append(input())
    print("Digite o preço do livro:")
    preco = input()
    livros[codigo] = (nome, num_autores, autores, preco)
    print("Deseja cadastrar outro livro? (S/N)")
    op = input().upper()
    print("#" * 20)
print("Escolha uma opção:")
print("1 - Pesquisar pelo código")
print("2 - Pesquisar pelo nome")
print("3 - Listar livros a cima de R$ 50,00")
consulop = int(input())
if consulop == 1:
    print("Digite o código do livro:")
    codigo = input()
    if codigo in livros:
        print(f"Nome: {livros[codigo][0]}")
        print(f"Número de autores: {livros[codigo][1]}")
        print(f"Autores: {', '.join(livros[codigo][2])}")
        print(f"Preço: R$ {livros[codigo][3]}")
    else:
        print("Livro não encontrado.")
elif consulop == 2:
    print("Digite o nome do livro:")
    nome = input()
    for k, v in livros.items():
        if v[0] == nome:
            print(f"Código: {k}")
            print(f"Número de autores: {v[1]}")
            print(f"Autores: {', '.join(v[2])}")
            print(f"Preço: R$ {v[3]}")
            break
        else:
            print("Livro não encontrado.")
elif consulop == 3:
    for k, v in livros.items():
        if float(v[3]) > 50.00:
            print(f"Código: {k}")
            print(f"Nome: {v[0]}")
            print(f"Número de autores: {v[1]}")
            print(f"Autores: {', '.join(v[2])}")
            print(f"Preço: R$ {v[3]}")
else:
    print("Opção inválida.")