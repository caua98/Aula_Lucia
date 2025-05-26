voos = {}
pessoas = {}
def cadastrar_voo():
    codigo = input("Digite o código do voo: ")
    if codigo in voos:
        print("Código de voo já cadastrado.")
        return
    origem = input("Digite a origem do voo: ")
    escalas = int(input("Digite o número de escalas do voo: "))
    preco = float(input("Digite o preço do voo: "))
    destino = input("Digite o destino do voo: ")
    data = input("Digite a data do voo (dd/mm/aaaa): ")
    hora = input("Digite a hora do voo (hh:mm): ")
    capacidade = int(input("Digite a capacidade do voo: "))
    
    voos[codigo] = {
        "origem": origem,
        "destino": destino,
        "Escalas": escalas,
        "data": data,
        "hora": hora,
        "Preco": preco,
        "capacidade": capacidade,
        "passageiros": [] 
    }
    
def vender_passagem():
    cpf = input("Digite o CPF do passageiro: ")
    if cpf in pessoas.keys():
        print("Passageiro já cadastrado.")
        return
    nome = input("Digite o nome do passageiro: ")
    documento = input("Digite o documento do passageiro (RG): ")
    telefone = input("Digite o telefone do passageiro: ")
    email = input("Digite o email do passageiro: ")
    
    pessoas[cpf] = {
        "nome": nome,
        "documento": documento,
        "telefone": telefone,
        "email": email
    }
    
    codigo_voo = input("Digite o código do voo para cadastrar o passageiro: ")
    
    if codigo_voo in voos:
        if cpf in voos[codigo_voo]["passageiros"]:
            print("Passageiro já cadastrado nesse voo.")
            return
        elif len(voos[codigo_voo]["passageiros"]) < voos[codigo_voo]["capacidade"]:
            voos[codigo_voo]["passageiros"].append({"cpf": cpf, **pessoas[cpf]})
            print(f"Passageiro {nome} cadastrado com sucesso no voo {codigo_voo}.")
        else:
            print(f"O voo {codigo_voo} está cheio.")
    else:
        print(f"Voo {codigo_voo} não encontrado.")

def listar_voos_disponíveis():
    disponiveis = []
    for codigo in voos:
        if len(voos[codigo]["passageiros"]) < voos[codigo]["capacidade"]:
            disponiveis.append(codigo)
    if disponiveis:
        print("Voos disponíveis:")
        print("\n".join(disponiveis))
    else:
        print("Nenhum voo disponível no momento.")

def consultar_voo():
    codigo = input("Digite o código do voo: ")
    if codigo in voos:
        voo = voos[codigo]
        print(f"Voo {codigo}:")
        print(f"Origem: {voo['origem']}")
        print(f"Destino: {voo['destino']}")
        print(f"Escalas: {voo['Escalas']}")
        print(f"Data: {voo['data']}")
        print(f"Hora: {voo['hora']}")
        print(f"Preço: R$ {voo['Preco']:.2f}")
        print(f"Capacidade: {voo['capacidade']}")
        print(f"Passageiros cadastrados: {len(voo['passageiros'])}/{voo['capacidade']}")
    else:
        print("Voo não encontrado.")

def consultar_voo_cidade():
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    encontrados = []
    for codigo, voo in voos.items():
        if voo["origem"].lower() == origem.lower() and voo["destino"].lower() == destino.lower():
            encontrados.append(codigo)
    if encontrados:
        print("Voos encontrados:")
        print("\n".join(encontrados))
    else:
        print("Nenhum voo encontrado.")

def cancelar_passagem():
    cpf = input("Digite o CPF do passageiro: ")
    codigo_voo = input("Digite o código do voo: ")
    
    if codigo_voo in voos and cpf in pessoas:
        # Verifica se o CPF está na lista de passageiros do voo
        for passageiro in voos[codigo_voo]["passageiros"]:
            if passageiro["cpf"] == cpf:
                voos[codigo_voo]["passageiros"].remove(passageiro)
                print(f"Passagem cancelada com sucesso para o passageiro {pessoas[cpf]['nome']} no voo {codigo_voo}.")
                return
        print("Passageiro não encontrado nesse voo.")
    else:
        print("Voo ou passageiro não encontrado.")

def listar_passageiros_voo():
    codigo_voo = input("Digite o código do voo: ")
    if codigo_voo in voos:
        passageiros = voos[codigo_voo]["passageiros"]
        if passageiros:
            print(f"Passageiros do voo {codigo_voo}:")
            for passageiro in passageiros:
                print(f"- {passageiro['nome']}")
        else:
            print("Nenhum passageiro cadastrado nesse voo.")
    else:
        print("Voo não encontrado.")

op = "S"
while op == "S":
    print("#" * 30)
    print("1 - Cadastrar voo")
    print("2 - Vender passagem")
    print("3 - Listar voos disponíveis")
    print("4 - Consultar voo")
    print("5 - Consultar voo por cidade")
    print("6 - Cancelar passagem")
    print("7 - Listar passageiros de um voo")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        cadastrar_voo()
    elif opcao == 2:
        vender_passagem()
    elif opcao == 3:
        listar_voos_disponíveis()
    elif opcao == 4:
        consultar_voo()
    elif opcao == 5:
        consultar_voo_cidade()
    elif opcao == 6:
        cancelar_passagem()
    elif opcao == 7:
        listar_passageiros_voo()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")
    