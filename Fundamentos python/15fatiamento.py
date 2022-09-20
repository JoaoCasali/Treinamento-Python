# Fatiamento é utilizado para retirar trechos de de uma determinada sequencia 
lista = ["Morango", "Laranja", "Uva"]

# [começo:fim-1:passos] o fatiamento sempre para um número antes do número selecionado 
print(lista[0:2]) # dessa forma pegaremos apenas os dois primeiros indices de uma lista
# listar e tuplas são fatiadas da mesma forma

# fatiamento tbm poderá ser usado em strings
texto = "Olá mundo, sou um dev python!!"

print(texto[11:]) # caso eu coloque apenas 11: ele listará até o final
print(texto[:9]) # caso eu coloque apenas :9 ele listará do inicio até o fim
