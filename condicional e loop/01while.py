# x, soma = 0, 0
# while x < 10:
#     n = float(input("Digite um numero: "))
#     soma += n
#     x+=1
#
# media = soma/10
# print("Media: ", media)

# alunos = int(input("Quantos alunos: "))
# x = 1
# soma = 0
# while x <= alunos:
#     n = float(input(f"Digite a nota do aluno {x}: "))
#     soma += n
#     x += 1
# media = soma/alunos
# print("Media de nota na sala: ", media)

# n1 = int(input("Digite um numero: "))
# n2 = int(input("Dividido por: "))
#
# while n2 == 0:
#     n2 = int(input("Segundo numero, invalido digite outro que seja diferente de zero: "))
#
# div = n1/n2
# print(div)

# senha = input("Digite a senha: ")
# t = 3
# print("---------- Login no sistema ----------\n")
# while t != 0:
#     tent = input("Digite sua senha: ")
#     if tent != senha:
#         t-=1
#         print(f"Senha errada. Mais {t} tentativa(s)\n")
#         if t == 0:
#             print("Conta bloqueada")
#     else:
#         t = 0
#         print("Login realizado com sucesso!")

# exit = "y"
# while exit == "y" or exit == "Y" or exit == "Yes" or exit == "yes":
#     n1 = float(input("Digite a primeira nota: "))
#     while n1 > 10 or n1 < 0:
#         n1 = float(input("Nota invalida, digite no intervalo de 0 à 10: "))
#
#     n2 = float(input("Digite a segunda nota: "))
#     while n2 > 10 or n2 < 0:
#         n2 = float(input("Nota invalida, digite no intervalo de 0 à 10: "))
#
#     media = (n1+n2)/2
#
#     print("Media: ", media)
#
#     exit = input("Deseja continuar? y/n \n")
#
# print("Obrigado por utilizar a calculadora de media! ")
# medias = 0
# alunos = int(input("Quantos alunos? "))
# for x in range(alunos):
#     n1 = float(input("Digite a primeira nota: "))
#     while n1 > 10 or n1 < 0:
#         n1 = float(input("Nota invalida, digite no intervalo de 0 à 10: "))
#
#     n2 = float(input("Digite a segunda nota: "))
#     while n2 > 10 or n2 < 0:
#         n2 = float(input("Nota invalida, digite no intervalo de 0 à 10: "))
#
#     media = (n1+n2)/2
#
#     print("Media: ", media)
#     medias += media
#
# total = medias/alunos
# print("Media de notas na sala: ", total)
# print("Obrigado por utilizar a calculadora de media! ")

n = int(input("Digite um numero: "))
for x in range(1, n+1):
    for y in range(1, x+1):
        print(x, end=" ")
    print()
    # print(x*str(x), end=" ")