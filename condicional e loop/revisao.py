# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
#
# media = (n1+n2)/2
#
# print("Media do aluno: ", media)

# soma = 0
# for i in range(2):
#     nota = float(input("Digite uma nota: "))
#     while nota > 10 or nota < 0:
#         nota = float(input("Digite uma nota de 0 a 10: "))
#     soma += nota
# media = soma/2
#
# print("Media do aluno: ", media)

# x = int(input("Quantas notas você vai adicionar? "))
# notas = [0.0] * x
#
# for n in range(len(notas)):
#     notas[n] = float(input("Digite uma nota: "))
#
# media = sum(notas) / len(notas)
#
# print("A media é: ", media)

# n = "s"
#
# while n == "s":
#     n = int(input("Digite um numero: "))
#     while n == 0:
#         n = int(input("Digite um numero diferente de 0: "))
#     if n > 0:
#         print("Numero positivo!")
#     else:
#         print("Numero negativo!")
#
#     n = input("Deseja continuar? s/n ")

# op = "s"
# while op == "s":
#     idade = int(input('Digite a idade: '))
#     anoAtual = 2024
#     x = input("Você já fez aniversário esse ano? ")
#     if x == 's':
#         anoNasc = anoAtual - idade
#     elif x == 'n':
#         anoNasc = anoAtual - idade - 1
#
#     print("Você nasceu em ", anoNasc)
#     op = input("Deseja realizar novamente? s/n \n")

# maior = 0
# for i in range(3):
#     n = int(input("Digite um numero: "))
#     if n > maior:
#         maior = n
# print("Maior é ", maior)

# n1 = int(input("Digite o primeiro numero: "))
# n2 = int(input("Digite o segundo numero: "))
# n3 = int(input("Digite o terceiro numero: "))
# maior = 0
#
# if n1 > n2:
#     if n1 > n3:
#         maior = n1
#     else:
#         maior = n3
# elif n2 > n3:
#     maior = n2
# else:
#     maior = n3
#
# print("O maior é ", maior)
n = 0
while n != -99:
    n = int(input("Digite um numero ou -99 para sair: "))
    if n == -99:
        break
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")
