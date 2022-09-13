nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média é: {media}")

# if é onde se inicia a estrutura, pode ser traduzido como "se"
# sua sintaxe é if (bloco condicional):
# uma outra parte da estrutura é o else, pode ser traduzido como "se não". Ele é utilizado quando nenhum caso foi compativel
# por ultimo temos o elif, não se tem uma tradução exata mas serve como um intermedário entre o if e o else
# Sua sintexe é elif (bloco condicional):
if media > 7.0:
    print("Você está acima da média!")

elif media == 7.0: 
    print("Você está na média!")

elif media >= 5.0 < 7.0: 
    print("Você pode solicitar a recuperação!")

elif media >= 4.0 < 5.0: 
    print("Você deve procurar o professor!")

else:
    print("Você não atingiu o esperado!")