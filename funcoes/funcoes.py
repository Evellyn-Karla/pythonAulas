def oi(nome):
    print(nome)


def numeros(n):
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print(f"{y} ", end="")
        print()


def vogais(t):
    nv, vaz, m = 0, 0, 0
    for i in t:
        if i in "aeiouAEIOU":
            nv += 1
        if i == " ":
            vaz += 1
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            m += 1
    con = len(t) - nv
    let = len(t) - vaz
    min = len(t) - m - vaz
    print(f"Vogais: {nv}, Consoantes: {con}, Espaços: {vaz}, Letras: {let}, Maiusculos: {m}, Minúsculos: {min}")


def estoque(qtd, valorUn):
    valort = qtd * valorUn
    return valort


def soma(n):
    x = len(n)
    total = 0
    for i in range(x):
        total += n[i]
    return total


def contInverso(t):
    let = 0
    print(t[::-1])
    for i in t:
        if i not in " .,;:-!?":
            let += 1
    print("\nLetras: ", let)


# li = [10, 12, 12, 4, 4, 5, 31, 9]

def unicos(li):
    tam = len(li)
    att = []
    for i in li:
        if i not in att:
            att.append(i)
    print(att)


def primos(n):
    if n == 1 or n % 2 == 0:
        return n, "não é primo"
    for i in range(2, n):
        if n % i == 0:
            return n, "é primo"
    return n, "não é primo"
