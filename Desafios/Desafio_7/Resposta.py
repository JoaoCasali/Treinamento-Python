nomeCompleto = str(input("Digite seu nome completo: "))

def primeiroNome(nome:str):
    Pnome = nome.split()[0]
    return Pnome

def ultimoNomeMaisculo(nome:str):
    UltimpNome = nome.split()[-1]   
    return UltimpNome.upper()

def inicialMaiscula(nome:str):
    return nome.title()

def separarLetras(nome:str):
    nomeJunto =  nome.replace(" ", "")
    listaNome = list(nomeJunto)
    nomeSeparado = ' '.join(listaNome)
    return nomeSeparado.upper()

def changeToX(nome:str):
    listaNome = nome.split()
    changedStr = []
    for i in range(len(listaNome)):
        auxiliar = list(listaNome[i])
        auxiliar[0] = "x"
        changedStr.append(''.join(auxiliar))
    return ' '.join(changedStr)

Pnome = primeiroNome(nomeCompleto)
ultimpNome = ultimoNomeMaisculo(nomeCompleto)
inicialM = inicialMaiscula(nomeCompleto)
nomeSeparado = separarLetras(nomeCompleto)
nomeX = changeToX(nomeCompleto)

print(f"""
    Primeiro nome: {Pnome}
    Ultimo nome em Maisculo: {ultimpNome}
    Iniciais maiusculas: {inicialM}
    Letras separadas: {nomeSeparado}
    Nome com iniciais X: {nomeX}
""")