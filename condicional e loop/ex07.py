n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = (n1 + n2 + n3) / 3

print(round(media, 2))
print("%.1f" % media)

if media >= 7:
    print("Aluno aprovado")
elif media >= 4: (
    print("Aluno em recuperação"))
else:
    print("Aluno reprovado")
