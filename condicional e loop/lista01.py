# lista = [1, 2, 3, 4]
#
# for i in lista:
#     print(i, end=" ")
#
#
# print("\nTotal ", len(lista))
# # for x in range(3):
# #     print(lista[x])

# idade = [20,5,16,27,50]
#
# for x in range(len(idade)):
#     print(idade[x], end=" ")


# notas = [0, 0, 0, 0, 0]
# soma, acima, media = 0, 0, 0
# for x in range(len(notas)):
#     notas[x] = float(input("Digite o nota:  "))
#
# for y in range(len(notas)):
#     soma += notas[y]
#     media = soma/len(notas)
#
# for z in range(len(notas)):
#     if notas[z] >= media:
#         acima += 1
#
# print(f"A media da turma é: {media}, alunos que passaram: {acima}")


# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# x = 0
#
# for x in range(len(a)):
#     a[x] = int(input("Digite o numero: "))
#
# x = int(input("Digite o x: "))
#
# for y in range(len(a)):
#     m[y] = a[y]*x
#
# print(m)

nums = [0, 0, 0, 0, 0]

for x in range(len(nums)):
    nums[x] = int(input("Digite os numeros: "))

print()

for y in range(len(nums)-1, -1, -1):
    print(nums[y], end=" ")