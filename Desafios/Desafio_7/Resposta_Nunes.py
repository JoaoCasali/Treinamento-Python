estoque = []

def registrar():
    print()
    produto = [str(input("Nome do produto: ")), float(input("Preço do produto: ")), int(input("Quantidade do produto: "))]
    produto.append((len(estoque) // 4) + 1)
    print()
    if produto[0] in estoque:
        pass
    else:
        estoque.extend(produto)

def procuraId(id_num):
    if id_num > len(estoque) // 4:
        print("O número de ID especificado ainda não foi registrado.")
    else:
        ids_nome = estoque[::4]
        ids_preço = estoque[1::4]
        ids_quant = estoque[2::4]
        print(f"\nProduto: {ids_nome[id_num - 1]}\nID: {id_num}\nPreço: {ids_preço[id_num - 1]}\nQuantia: {ids_quant[id_num - 1]}")

def procuraNome(nome):
    if nome in estoque:
        print(f"\nProduto: {estoque[estoque.index(nome)]}\nID: {estoque[estoque.index(nome) + 3]}\nPreço: {estoque[estoque.index(nome) + 1]}\nQuantia: {estoque[estoque.index(nome) + 2]}\n")
    else:
        print("Produto não encontrado, confira as letras maiúsculas e minúscalas, ou se o nome já foi mesmo registrado.")

def listagem():
    nomes = estoque[::4]
    preços = estoque[1::4]
    quantias = estoque[2::4]
    ids = estoque[3::4]
    print()
    for i in range(1, len(estoque) // 4 + 1):
        print(f"Produto: {nomes[i - 1]}\nID: {ids[i - 1]}\nPreço: {preços[i - 1]}\nQuantia: {quantias[i - 1]}\n")

console = True
while console == True:
    menu = input("Opções:\n1)Registrar um produto.\n2)Lista de produtos registrados.\n3)Procurar um produto através do nome.\n4) Procurar um produto através do ID.\n5)Desligar sistema.\nEscolha: ")
    if menu == "1":
        registrar()
    elif menu == "2":
        listagem()
    elif menu == "3":
        procuraNome(input("Digite o nome do produto que procura: "))
    elif menu == "4":
        procuraId(int(input("Digite o ID do produto que procura: ")))
    elif menu == "5":
        console = False
    else:
        print("\nOpção digitada é inválida ou inexistente.\n")