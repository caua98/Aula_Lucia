voos = {}
pessoas = {}
def cadastrar_voo():
    codigo = input("Digite o código do voo: ")
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
    
def cadastrar_passageiro():
    cpf = input("Digite o CPF do passageiro: ")
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
        if len(voos[codigo_voo]["passageiros"]) < voos[codigo_voo]["capacidade"]:
            voos[codigo_voo]["passageiros"].append(pessoas[cpf])
            print(f"Passageiro {nome} cadastrado com sucesso no voo {codigo_voo}.")
        else:
            print(f"O voo {codigo_voo} está cheio.")
    else:
        print(f"Voo {codigo_voo} não encontrado.")