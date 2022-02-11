from datetime import date
SEMANA = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
dia = date.today().weekday()
doses = int(input("Digite a quantidade de doses que devão ser tomadas: "))
intervalo = int(input("Digite o intervalo de dias entre as doses: "))
for d in range(doses):
    for i in range(intervalo):
        dia += 1
        if dia == 7:
            dia =0

print(f"A ultima dose será em um(a) {SEMANA[dia]}")