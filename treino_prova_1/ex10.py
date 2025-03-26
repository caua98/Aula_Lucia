notas = 0
alunos = int(input("Digite a quantidade de alunos: "))
for a in range(alunos):
    notas += float(input("Digite a nota do aluno: "))
print(f"A média das notas é {notas/alunos:.2f}")