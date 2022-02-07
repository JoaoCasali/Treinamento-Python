x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
if x < y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
if z > maior:
    print(z, maior, menor)
elif z < y:
    print(maior, menor, z)
else:
    print(maior, z, menor)