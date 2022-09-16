# funções built-in são ferramentas que vem com o python, elas ajudam a realizar tarefas simples e comuns aos programadores
# no geral.
# para chamar uma função built-in basta apenas digitar o nome dela colocando em seguida ()

listaNumeros = [10, 128, 31, 321]

# a função sum soma todos os itens de uma sequencia, podendo ser lista, tuplas, dicionários, etc.
# No caso de dicionários, ele somará os indices e não os valores
soma = sum(listaNumeros)
print(soma)

# len conta a quantidade de indices em uma sequencia
print(len(listaNumeros)) # funções podem ser chamadas em qualquer lugar

# eval transforma strings em códigos python 
calculoComplexo = eval('(2*4)/2 + 21**5')

print(calculoComplexo)

# round arredonda números com base na regra matemática
arredondado = round(10.8)
print(arredondado)

# para mais informações sobre as funções built-in acesse a documentação python
# https://docs.python.org/pt-br/3.6/library/functions.html