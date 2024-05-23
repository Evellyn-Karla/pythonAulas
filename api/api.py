import requests




def verificarCep():
    cepIn = input("Digite o cep: ")
    while len(cepIn) != 8:
        cepIn = input("Digite um cep valido (8 numeros): ")
    consulta = requests.get(f"https://viacep.com.br/ws/{cepIn}/json/")
    dados = consulta.json()
    print(f"CEP: {dados['cep']}, Logradouro: {dados['logradouro']}, Bairro: {dados['bairro']}, "
          f"Localidade: {dados['localidade']}, UF: {dados['uf']}\n")


def sair():
    print("Xauzin")
def menu():
    op = {
        1: verificarCep,
        2: sair
    }
    valor = 0
    while valor != 2:
        valor = int(input("Digite 1 para Verificar CEP ou 2 para sair "))
        if valor in op:
            op[valor]()
        else:
            print("Opção invalida")

menu()