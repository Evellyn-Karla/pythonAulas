from funcoes import *

# t = input("Digite uma frase: ")
# vogais(t)

# nome = input("Digite o nome do produto: ")
# qtd = int(input("Digite a quantidade do produto: "))
# valor = float(input("Digite o valor unitário do produto: "))
#
# valort = estoque(qtd, valor)
#
# print(f"\n========== \nEstoque de {nome} \nQtd: {qtd}\nValor total no estoque: R${valort:.2f}")

# x = int(input("Qnts n? "))
# n = [0]*x
# for i in range(x):
#     n[i] = int(input("Digite um numero: "))

# n = []
# v = "0"
#
# while v != "=":
#     v = input("Calcular:\n").strip()
#     if v != "=":
#         n.append(int(v))
#
# soma = soma(n)
# print("Soma:", soma)

# texto = input("Digite: ")
#
# contInverso(texto)

# li = (input("Digite os valores: ").split(', '))
# unicos(li)

n = int(input("Digite um numero: "))
b = primos(n)
if b == 0:
    print("Não é primo")
else:
    print("É primo")