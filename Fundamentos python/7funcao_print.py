# input é uma função utilizada para obter informações atraves do terminal
nome = input("Digite seu nome: ") # inputs retornam sempre uma string
idade = int(input("Digite sua idade: ")) # convertendo a string de retorno do input em um inteiro
salario = float(input("Digite seu salário: ")) # convertendo para float

# Utilizando interpolação para imprimir os dados no terminal
print(f'Olá!, meu nome é {nome}, tenho {idade} e ganho {salario} por mês!')