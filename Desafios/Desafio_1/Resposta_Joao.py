lista = [0, 1]
qtde = int(input("Digite o tamanho desejado: "))
for i in range(1, qtde - 1):
    lista.append(lista[i] + lista[i-1])
print(lista)