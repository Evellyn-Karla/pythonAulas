import cnx
import mysql.connector
import os

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="desafioC"
)

cursor = banco.cursor()


def ler():
    req = 'select * from alunos;'  # input('Digite o codigo sql: ')
    cursor.execute(req)
    res = cursor.fetchall()

    for x in res:
        print(x)


def inserir():
    nome1 = input("Digite o nome: ")
    telefone1 = input("Digite o telefone: ")

    sql = 'insert into alunos (nome) value(%s);'
    sqlTel = 'insert into telefones(matricula, numero) value (%d, %s);'

    data = [(nome1)]
    cursor = cnx.cursor()
    cursor.execute(sql, nome1)
    banco.commit()

    userid = cursor.lastrowid
    data1 = (userid, telefone1)
    cursor.execute(sqlTel, data1)
    banco.commit()
    print("Adicionado com sucesso!")



def sair():
    print("Xauzin")
    cursor.close()
    banco.close()
    return


op = 0


def menu():
    os.system('cls')
    ops = {
        1: ler,
        2: inserir
    }

    op = 0

    while op != 3:
        print("\n1: Ler\n2: Inserir\n3: Sair\n")
        op = int(input("Digite a opção: "))
        if op == 3:
            sair()
            break

        if op in ops:
            ops[op]()
        else:
            print("Opção não existente")


menu()








