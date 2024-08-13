# Dicionário para armazenar os nomes das pessoas presentes no IA3, organizados por letra
presenca = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}

# Função para adicionar uma pessoa à lista de presença no IA3
def adicionar_presenca(nome, empresa):
    nome = nome.title()  # Padroniza o nome com a primeira letra maiúscula
    empresa = empresa.title()  # Padroniza o nome da empresa
    letra_inicial = nome[0]  # Obtém a primeira letra do nome
    
    # Verifica se a pessoa já está na lista
    if letra_inicial in presenca and not any(p['nome'] == nome for p in presenca[letra_inicial]):
        presenca[letra_inicial].append({'nome': nome, 'empresa': empresa})
        print(f"{nome} da empresa {empresa} adicionado à lista de presença.")
    elif any(p['nome'] == nome for p in presenca[letra_inicial]):
        print(f"{nome} já está na lista de presença.")
    else:
        print(f"Erro: Não foi possível adicionar {nome}.")

# Função para remover uma pessoa da lista de presença
def remover_presenca(nome):
    nome = nome.title()  # Padroniza o nome com a primeira letra maiúscula
    letra_inicial = nome[0]  # Obtém a primeira letra do nome
    
    # Encontra e remove a pessoa da lista, se ela estiver presente
    if letra_inicial in presenca:
        for pessoa in presenca[letra_inicial]:
            if pessoa['nome'] == nome:
                presenca[letra_inicial].remove(pessoa)
                print(f"{nome} removido da lista de presença.")
                return
    print(f"{nome} não está na lista de presença.")

# Função para listar todas as pessoas presentes
def listar_presenca():
    print("Lista de presença:")
    for letra in sorted(presenca.keys()):
        if presenca[letra]:  # Se houver nomes na lista para a letra atual
            print(f"{letra}:")
            for pessoa in sorted(presenca[letra], key=lambda x: x['nome']):
                print(f"  - {pessoa['nome']} (Empresa: {pessoa['empresa']})")
    if not any(presenca.values()):
        print("Nenhuma pessoa na lista de presença.")

# Exemplo de uso
adicionar_presenca("Maria", "Empresa X")
adicionar_presenca("João", "Empresa Y")
adicionar_presenca("Ana", "Empresa Z")
listar_presenca()
remover_presenca("João")
listar_presenca()