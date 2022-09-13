soma = 2 + 2 # soma os dois números
print("Soma:", soma)
subtracao = 2 - 2 # subtrai os dois números
print("Subtração:", subtracao)
divisao = 2 / 2 # divide os dois números, sempre retorna um float
print("Divisão:", divisao)
multiplicacao = 2 * 2 # multiplica os dois números
print("Multiplicação:", multiplicacao)
exponenciacao = 2 ** 2 # eleva um número a outro
print("Exponenciação:", exponenciacao)

divisao_exata = 2 // 2 # ignora o resto da divisão, ponto flutuante, retorna sempre um inteiro
print("Divisão exata:", divisao_exata)

resto_divisao = 3 % 2 # mostra apenas o resto da divisão de um número, retorna sempre um inteiro
print("Resto da divisão:", resto_divisao)

# em expressões matemáticas existe uma ordem de procedencia dos calculos, no python é o mesmo!
# A ordem é a seguinte:
# Os parenteses possuem prioridade máxima
# Em seguida exponenciação, divisão, divisão exata e resto de divisão
# Por ultimo soma e subtração


# o parenteses pode ser utilizado para dar prioridade a calculos
media = (5 + 8) / 2
print("média entre 5 e 8 é", media)
