total, fora = 0, 0
for x in range(10):
    n = int(input("Digite um numero: "))
    if n > 9 and n < 21:
        total += 1
fora = 10 - total
print("No intervalo: ", total, "\nFora: ", fora)
