hora1 = int(input("Escreva a hora da primeira entrada: "))
min1 = int(input("Escreva os minutos da primeira entrada: "))
hora2 = int(input("Escreva a hora da segunda entrada: "))
min2 = int(input("Escreva os minutos da segunda entrada: "))
saida = 0
if min1 < 10:
    print(f"\nEntrada 1: {hora1}:0{min1}")
else:
    print(f"\nEntrada 1: {hora1}:{min1}")
if min2 < 10:
    print(f"Entrada 2: {hora2}:0{min2}\n")
else:
    print(f"Entrada 2: {hora2}:{min2}\n")
minS = min1 + min2
if minS >= 60:
    minS = minS - 60
    saida = hora1 + hora2 + 1
else:
    saida = hora1 + hora2
if saida > 12 and saida < 25:
    saida = saida - 12
elif saida > 24:
    saida = saida - 24
if minS < 10 and saida > 10:
    print(f"Saida: {saida}:0{minS}")
else:
    print(f"Saida: {saida}:{minS}")