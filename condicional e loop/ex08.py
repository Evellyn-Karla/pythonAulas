time1 = input("Primeiro time: ")
gols1 = int(input("Gols dele: "))

time2 = input("Segundo time: ")
gols2 = int(input("Gols dele: "))

if gols1 == gols2:
    print("EMPATE")
elif gols1 > gols2:
    print("Vencedor: ", time1)
else:
    print("Vencedor: ", time2)
