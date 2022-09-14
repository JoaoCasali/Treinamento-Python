from random import choice # importando a função choice
# abrindo o arquivo txt
arq = open("Desafios/Desafio_10/listaDeNomes.txt", 'r', encoding= "UTF-8")
# obtendo os dados do arquivo txt, gerando uma lista
nomes_brutos = arq.readlines()
# fechando o arquivo
arq.close()
# limpando os dados, pois eles vem com quebra de linhas no final, o que atrapalha a leitura
# map = aplica uma função em todos os itens de uma lista
# lambda = cria uma mini função, nesse caso está substituindo os caracteres \n por vazio
nomes_limpos = list(map(lambda x: x.replace('\n', ''), nomes_brutos))

# imprimindo no terminal
print(f"O nome sorteado foi: {choice(nomes_limpos)}")