data = int(input("Digite uma data no formato DDMMAAAA: "))
print(f" dia: {data // 1000000}, mes: {(data % 1000000) // 10000}, ano:{data % 10000}")