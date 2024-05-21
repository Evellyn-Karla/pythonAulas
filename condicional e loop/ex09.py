litros = float(input("Digite o numero de litros: "))
tipoC = input("Digite 'G' para Gasolina e 'E' para Etanol: ").upper()

valor = 0
pG = 5.8
pE = 4.9


if tipoC == "G":
    valor = litros * pG
    print("Valor total: R$%.2f" % valor)
elif tipoC == "E":
    valor = litros * pE
    print("Valor total: R$%.2f" % valor)
else:
    print("Tipo inexistente")



