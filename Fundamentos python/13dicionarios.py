# dicionários são utilizadas para armazenar dados em uma mesma variavel
# dicionário são declarados como uma variável comum, porém, sua sintaxe é um pouco distinta
# são declarados com {}
# a diferença dele para tuplas e lista é que os indices não são gerados pelo computador e sim pelo programador
# dessa forma, o dicionário trabalha de forma chave/valor 

dicionario = {'fruta': "banana",'cor': "amarela"}

# print padrão do dicionário
print(dicionario)

# acessando cada indice de forma separada
print(dicionario['fruta'], dicionario['cor'])
# repare que ao invez de um número foi colocado as chaves descritas anteriormente

# adicionando uma nova chave ao dicionário
dicionario['citrica'] = False

print(dicionario)

# mudando um valor de uma chave
dicionario['cor'] = "verde"

print(dicionario)
