from datetime import date
dia = date.today().weekday()
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

dose, pausa = int(input("Quantas doses de remédio deve tomar no total? R: ")), int(input("Quantos dias de intervalo entre as doses? R: "))
semana = semana * (dose * pausa)

while dose != 1:
    dose -= 1
    dia = dia + pausa + 1
    
print(f"Você tomará sua última dose do remédio em um(a) {semana[dia]}, totalizando {dia - date.today().weekday() + 1} dias tomando o remédio.")