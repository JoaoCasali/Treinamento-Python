import random

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?ãÃõÕ"

def setChave(chave = None):
    if chave == None:
        chave = random.randint(100,999)
    random.seed(chave)
    return chave

def gerarDicio(caracteres:str):
    dicio = {}
    for i in range(len(caracteres)):
        valor = random.randint(1,999)
        while valor in dicio.values():
            valor = random.randint(1,999)
        dicio[caracteres[i]] = valor
    
    return dicio

def criptografar(mensagem:str, dicio:dict):
    mensagem = list(mensagem)
    mensagemCriptografada = []
    for l in mensagem:
        mensagemCriptografada.append(str(dicio[l]))
    
    criarArquivo(' '.join(mensagemCriptografada))
    return ' '.join(mensagemCriptografada)
    
def descriptografar(mensagem:str, dicio:dict):
    mensagem = mensagem.split(" ")
    mensagemDescriptografada = []
    for i in mensagem:
        for carac, valor in dicio.items():
            if int(i) == valor:
                mensagemDescriptografada.append(carac)
    
    
    return ''.join(mensagemDescriptografada)

def criarArquivo(mensagem):
    arq = open("Desafios/Desafio_9/Criptografia.txt", 'w')
    arq.write(mensagem)
    arq.close()

def lerArquivo(nomeArq):
    arq = open(f'Desafio_9/{nomeArq}', 'r')
    mensagem = arq.read()
    arq.close()
    return mensagem    

opcao = int(input("""
    1 - Criptografar mensagem
    2 - Descriptografar mensagem
    R: """))

if opcao == 1:
    chave = setChave()
    dicio = gerarDicio(caracteres)
    mensagem = input("Digite sua mensagem: ")
    print(criptografar(mensagem, dicio))
    print(f"Sua chave de acesso é: {chave}")
    
elif opcao == 2:
    opcao1 = input("Deseja buscar a mensagem de um arquivo? (y/n): ")
    if opcao1 == 'y':
        mensagem = lerArquivo(input("Digite o nome do arquivo (Ex: arquivo.txt): "))    
    else:
        mensagem = input("Digite sua mensagem: ")
    setChave(int(input("Digite sua chave: ")))
    dicio = gerarDicio(caracteres)
    print(descriptografar(mensagem, dicio))