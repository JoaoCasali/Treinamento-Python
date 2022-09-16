dicionarios = {}
while True:
    print("(1) criar lista;\n(2) visualizar listas;\n(3) deletar lista;\n(4) Encerar código")
    opcao = int(input(f"Digite a opção desejada: "))
    if opcao == 1:
        chave = input("Digite o nome da lista: ")
        valor = input("Digite os itens da lista separados por virgula: ").split(",")
        dicionarios[chave] = valor
        print("="*8, "Lista adcionada!!", "="*8)
    
    if opcao == 2:
        print("="*8)
        for chave, valor in dicionarios.items():
            print(f'Lista : {chave}\nItens: {valor}')
        print("="*8)
    
    if opcao == 3:
        chave = input("Digite a lista que será deletada: ")
        dicionarios.pop(chave)
        print("="*8, "Lista removida!!", "="*8)

    if opcao == 4:
        break