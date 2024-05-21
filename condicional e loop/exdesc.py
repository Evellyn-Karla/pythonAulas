# for x in  range(10,0, -1):
#     print(x, end = " ")

# for x in range(101, 111):
#     print(x)

# n = int(input("Digite um numero: "))
# for x in range(1, n+1):
#     print(x)

neg = 0
for x in range(1, 11):
    n = int(input("Digite um numero: "))
    if n < 0:
        neg += 1
print(neg)