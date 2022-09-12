# Mascaras de substituição são usadas para colocar variáveis entre string de forma mais legivel
nome = 'Carlos'
idade = 20
salario = 1200.40

# Para fazer isso, abre-se chaves dentro das strings e, após elas, chama-se a função format e dentro dela coloca-se as
# variaveis desejadas.
print('Olá!, meu nome é {}, tenho {} e ganho {} por mês!'.format(nome, idade, salario))