num1, num2 = 0, 1

qnt = int(input("Quantos números da sequência de Fibonacci deseja imprimir: "))

if qnt == 1:
    print("0")
elif qnt == 2:
    print("0\n1")
else:
    print("0\n1")
    for i in range(0, qnt - 2):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3