soma, m = 0, 0
for x in range(10):
    n = float(input("Digite a nota: "))
    if n >= 0 and n < 11:
        m += 1
        soma += n
    else:
        print("Invalido")
if m > 0:
    media = soma/m
    print("A media é: %.1f" % media)
else:
    print("Tudo invalido")