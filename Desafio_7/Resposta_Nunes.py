def primeiroNome(nome):
    return nome.split()[0]

def ultimoNome(nome):
    return nome.split()[-1].upper()

def primeirasLetras(nome):
    letras = ""
    for i in nome.split():
        letras += i[0].capitalize()
    return letras

def maiusculaEspaçada(nome):
    nome = nome.upper()
    espaçado = ""
    for i in nome:
        if i == " ":
            continue
        espaçado += i
        espaçado += " "
    espaçado = espaçado[:-1]
    return espaçado

def substituirX(nome):
    nomes = nome.split()
    x = ""
    for i in nomes:
        x += i.replace(i[0], "X")
        x += " "
    x = x[:-1]
    return x

while True:
    pergunta = input("Digite um nome a ser manipulado: ")
    print("Primeiro nome:", primeiroNome(pergunta))
    print("Último nome maiúsculo:", ultimoNome(pergunta))
    print("Letras iniciais de cada nome:", primeirasLetras(pergunta))
    print("Nome maiúsculo e espaçado por letra:", maiusculaEspaçada(pergunta))
    print("Nome com letras iniciais substituídas por X:", substituirX(pergunta))