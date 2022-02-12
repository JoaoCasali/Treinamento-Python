# Função para gerar uma chave de acesso aleatória.
def gerarChave():
    import random
    chave = random.randrange(10000, 99999)
    return chave

# Função que recebe uma string e a converte em uma sequência numérica.
# Cada um dos pares da sequência representa um algarismo da mensagem inserida.
def transformarNumero(texto:str):
    letras_minuscula = {"a": "10", "b": "11", "c": "12", "d": "13", "e": "14", "f": "15", "g": "16", "h": "17", "i": "18", "j": "19", "k": "20", "l": "21", "m": "22", "n": "23", "o": "24", "p": "25", "q": "26", "r": "27", "s": "28", "t": "29", "u": "30", "v": "31", "w": "32", "x": "33", "y": "34", "z": "35"}
    letras_maiuscula = {"A": "36", "B": "37", "C": "38", "D": "39", "E": "40", "F": "41", "G": "42", "H": "43", "I": "44", "J": "45", "K": "46", "L": "47", "M": "48", "N": "49", "O": "50", "P": "51", "Q": "52", "R": "53", "S": "54", "T": "55", "U": "56", "V": "57", "W": "58", "X": "59", "Y": "60", "Z": "61"}
    caracteres = {" ": "62", ",": "63", ".": "64"}
    numero = ""
    for i in texto:
        if i in letras_minuscula:
            numero += letras_minuscula[i]
        elif i in letras_maiuscula:
            numero += letras_maiuscula[i]
        elif i in caracteres:
            numero += caracteres[i]
        else:
            continue
    numero = int(numero)
    return numero

# Função que multiplica o número gerado na função anterior por uma chave de acesso qualquer.
def criptografarNumero(numero:int, chave:int):
    msg_cript = numero * chave
    return msg_cript

# Função que descriptografa uma sequência gerada pela função anterior utilizando a mesma chave utilizada.
def descriptografarNumero(msg_cript:int, chave:int):
    msg_decript = msg_cript // chave
    msg_decript = str(msg_decript)
    return msg_decript

# Função que transforma o numero descriptografado novamente em um texto.
def transformarTexto(msg_decript:str):
    letras_minuscula = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17': 'h', '18': 'i', '19': 'j', '20': 'k', '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r', '28': 's', '29': 't', '30': 'u', '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z'}
    letras_maiuscula = {'36': 'A', '37': 'B', '38': 'C', '39': 'D', '40': 'E', '41': 'F', '42': 'G', '43': 'H', '44': 'I', '45': 'J', '46': 'K', '47': 'L', '48': 'M', '49': 'N', '50': 'O', '51': 'P', '52': 'Q', '53': 'R', '54': 'S', '55': 'T', '56': 'U', '57': 'V', '58': 'W', '59': 'X', '60': 'Y', '61': 'Z'}
    caracteres = {"62": " ", "63": ",", "64": "."}
    texto = ""
    num1 = msg_decript[::2]
    num2 = msg_decript[1::2]
    for i in range(0, len(msg_decript) // 2):
        par = num1[i] + num2[i]
        if par in letras_minuscula:
            texto += letras_minuscula[par]
        elif par in letras_maiuscula:
            texto += letras_maiuscula[par]
        elif par in caracteres:
            texto += caracteres[par]
    return texto

# Menu para testes :P
while True:
    menu = input("""
    Opções:
    1) Gerar uma chave de acesso para sua criptografia.
    2) Criptografar uma mensagem utilizando sua chave.
    3) Descriptografar uma mensagem utilizando sua chave.
    4) Encerrar sistema.
    R:""")
    if menu == "1":
        print(f"\nChave de acesso: {gerarChave()}")
    elif menu == "2":
        numero = transformarNumero(str(input("\nDigite o texto a ser criptografado: ")))
        chave = int(input("Digite sua chave de acesso: "))
        print(f"Mensagem: {criptografarNumero(numero, chave)}")
    elif menu == "3":
        msg_cript = int(input("\nDigite a mensagem criptografada: "))
        chave = int(input("Digite sua chave de acesso: "))
        msg_decript = descriptografarNumero(msg_cript, chave)
        print(f"Mensagem: {transformarTexto(msg_decript)}")
    elif menu == "4":
        break

# Sim João, eu ainda não acabei, sei que falta salvar em um arquivo de texto.