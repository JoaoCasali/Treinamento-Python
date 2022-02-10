data = int(input("Digite uma data: "))

meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

print(f"{data // 1000000} de {meses[data // 10000 % 100]} de {data % 10000}.")