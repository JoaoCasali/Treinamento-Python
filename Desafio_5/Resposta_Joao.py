from datetime import datetime 
CALENDARIO = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diaA, mesA, anoA = datetime.now().strftime('%d/%m/%Y').split("/")
def ContadorAMD(anoA, mesA, diaA, anoN, mesN, diaN, qtdeBisexto, tipo):
    anosVividos = anoA - anoN - 1
    mesesVividos = (anosVividos * 12) + (12 - mesN) + mesA - 1
    diasVividos = anosVividos * 365 + (CALENDARIO[mesN-1] - diaN) + diaA + qtdeBisexto
    for i in range(12 - mesN):
        diasVividos += CALENDARIO[mesN + i]
    for i in range(mesA - 1):
        diasVividos += CALENDARIO[i]
    if tipo == 2:
        diasVividos -= 1
    return anosVividos, mesesVividos, diasVividos 
diaN, mesN, anoN = input("Digite sua data de nacimento no formato DD/MM/AAAA: ").split("/")
diaA, mesA, anoA = int(diaA), int(mesA), int(anoA)
diaN, mesN, anoN = int(diaN), int(mesN), int(anoN)
qtdeBisexto = 0
for bi in range(anoN, anoA + 1):
    if bi % 4 == 0:
        qtdeBisexto += 1
if mesN <= mesA:
    if diaN <= diaA:
        anosVividos = anoA - anoN
        mesesVividos = (anosVividos * 12) - 1
        auxiliar = mesN + 1
        diasVividos = (anosVividos * 365) + diaA - diaN + qtdeBisexto
    else:
        anosVividos, mesesVividos, diasVividos = ContadorAMD(anoA, mesA, diaA, anoN, mesN, diaN, qtdeBisexto, 2)
elif mesN > mesA:
    anosVividos, mesesVividos, diasVividos = ContadorAMD(anoA, mesA, diaA, anoN, mesN, diaN, qtdeBisexto, 3)
print(f"Você viveu {anosVividos} anos, {mesesVividos} meses e {diasVividos} dias.")