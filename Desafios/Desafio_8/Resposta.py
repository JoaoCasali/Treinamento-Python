estoque = []
def gerarID(estoque):
    return len(estoque)

def formatoPrint(p):
    print(f"Id: {p['id']}")
    print(f"Nome: {p['nome']}")
    print(f"Preço: {p['preco']}")
    print(f"Quantidade em estoque: {p['qtde']}")
    print("----------------")

def gerarProdutos(estoque):
    for i in range(5):
        estoque.append({"id": gerarID(estoque), "nome": "produto " + str(i) , "preco": (i+1)*2, "qtde": (i+1) * 4})
    return estoque

def listarProdutos(estoque):
    for p in estoque:
        formatoPrint(p)

def procurarProduto(estoque, forma = 1, nome = "-"):
    if forma == 1:
        nomeP = input("Digite o nome para ser procurado: ") if nome == "-" else nome
        for p in estoque:
            if p['nome'] == nomeP:
                print("")
                formatoPrint(p)
                return True
        return False
    if forma == 2:
        idP = int(input("Digite o id para ser procurado: ")) 
        for p in estoque:
            if p['id'] == idP:
                print("")
                formatoPrint(p)
                return True
        return False

def adicionarProduto(estoque):
    nome = input("Digite o nome do produto: ")
    if procurarProduto(estoque, nome = nome):
        return print("\033[1;91mProduto com esse nome já existe!! ↑↑↑\033[0;0m")
    preco, qtde = float(input("Digite o preço do produto: ")), float(input("Digite a quantidade em estoque do produto: "))
    estoque.append({"id": gerarID(estoque), "nome": nome, "preco": preco, "qtde": qtde})
    return estoque

while True:
    print(""" 
Escolha uma das opções:
    1 - adicionar produtos
    2 - listar produtos
    3 - procurar por produto
    4 - Encerar o código""")
    opcao = int(input("    Digite: "))
    if opcao == 1:
        estoque = adicionarProduto(estoque)
    elif opcao == 2:
        print("")
        listarProdutos(estoque)
    elif opcao == 3:
        forma = int(input("Deseja procurar pelo nome (1) ou id (2): "))
        procurarProduto(estoque, forma)
    elif opcao == 5:
        estoque = gerarProdutos(estoque)