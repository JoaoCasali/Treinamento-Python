# listas são utilizadas para armazenar dados em uma mesma variavel
# Elas são declaradas como uma variável comum, apenas sendo sinalizada com []
lista = ["banana", "maçã", 'uva']

# print comum de uma lista
print(lista)

# para acessar itens especificos é necessário utilizar essa sintaxe: nomeVariavel[index]
# Index em python sempre começam no 0
# print acessando cada item por vez
print(lista[0], lista[1], lista[2])

# listas são muito uteis por suas funções
# para utilizar essas funções, deve-se apenas colocar um "." após o nome da variável lista e colocar o nome da função
# desejada segida de ()

# função para adicionar um item na lista
lista.append("laranja")

print(lista)

lista.remove("banana")
print(lista)

# Recomendo acessar as documentações do python para conhecer melhor essa funções built-in das listas
# https://www.python.org/doc/ 