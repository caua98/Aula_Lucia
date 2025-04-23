qntt_alunos = int(input("Quantos alunos você quer cadastrar?: "))
alunos = []
for i in range(qntt_alunos):
    nome = input(f"Nome do aluno {i + 1}: ").upper()
    t1 = float(input(f"Nota do Trabalho 1 do aluno {i + 1}: "))
    t2 = float(input(f"Nota do Trabalho 2 do aluno {i + 1}: "))
    p1 = float(input(f"Nota da Prova 1 do aluno {i + 1}: "))
    p2 = float(input(f"Nota da Prova 2 do aluno {i + 1}: "))
    mt = 0.4 * t1 + 0.6 * t2
    mp = (p1 + p2) / 2
    if mt >= 5 and mp >= 5:
        mf = 0.3 * mp + 0.7 * mt
    elif mt < 5 and mp < 5:
        if mt >= mp:
            mf = mp
        else:
            mf = mt
        
    aluno = [nome, [t1, t2], [p1, p2], [mt, mp], mf]
    alunos.append(aluno)
op2 = "S"
op = ""
print("######################################################")
print("Selecione uma opção a seguir:")
print("1 - Mostrar todos os alunos")
print("2 - Mostrar informações de um aluno específico")
print("3 - Mostrar aluno com maior maior média final")
print("4 - Mostrar aluno com menor média final")
print("5 - Mostrar percentual de alunos aprovados")

while op2 == "S":
    while op == "":
        op = int(input("Digite a opção desejada: "))

        if op == 1:
            print("######################################################")
            print("Alunos cadastrados:")
            for aluno in alunos:
                print(f"Nome: {aluno[0]}| Média Teórica: {aluno[3][0]} | Média Prática: {aluno[3][1]} | Média Final: {aluno[-1]}")
            print("######################################################")

        if op == 2:
            print("######################################################")
            nome = input("Digite o nome do aluno: ").upper()
            for aluno in alunos:
                if aluno[0] == nome:
                    print(f"Nome: {aluno[0]}| Notas Teóricas: {aluno[1]} | Notas Práticas: {aluno[2]} |Média Teórica: {aluno[3][0]} | Média Prática: {aluno[3][1]} | Média Final: {aluno[-1]}")
                    break
            else:
                print("Aluno não encontrado.")
            print("######################################################")

        if op == 3:
            maior = 0
            print("######################################################")
            for aluno in alunos:
                if aluno[-1] > maior:
                    maior = aluno[-1]
                    aluno_maior = aluno[0]
            print(f"Aluno com maior média final: {aluno_maior} | Média Final: {maior}")
            print("######################################################")
    
        if op == 4:
            menor = 11
            print("######################################################")
            for aluno in alunos:
                if aluno[-1] < menor:
                    menor = aluno[-1]
                    aluno_menor = aluno[0]
            print(f"Aluno com menor média final: {aluno_menor} | Média Final: {menor}")
            print("######################################################")

        if op == 5:
            print("######################################################")
            aprovados = 0
            for aluno in alunos:
                if aluno[-1] >= 5:
                    aprovados += 1
            percentual = (aprovados / qntt_alunos) * 100
            print(f"Percentual de alunos aprovados: {percentual}%")
            print("######################################################")
        
        op2 = input("Quer realizar mais uma consulta?(S/N): ").upper()
        if op2 == "S":
            op = ""