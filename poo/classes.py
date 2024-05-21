# class Nome:
#   def __init__ (self):  -- constructor

# class formato: PrimeiraSegunda
# metodo formato: primeiraSegunda

# ========= com var categorica ======================
# class Pessoa():
#     def __init__(self, nome, peso, idade, acao = ''):
#         self.nome = nome
#         self.peso = peso
#         self.idade = idade
#         self.acao = acao
#
#     def comer(self, comida=""):
#         if self.acao:
#             print(f'{self.nome} está ocupado {self.acao}')
#         else:
#             self.acao = "Comendo"
#             if comida == "":
#                 print(f'{self.nome} não foi comer')
#             else:
#                 print(f'{self.nome} foi comer {comida}')
#     def pararComer(self):
#         if self.acao == 'comendo':
#             print("João parou de comer")
#             self.acao = ''
#         else:
#             print(f'{self.nome} não está comendo')
#
#     def dormir(self, bool = True):
#         if self.acao == '':
#             if bool:
#                 self.acao = 'dormindo'
#                 print(f'{self.nome} está dormindo')
#             else:
#                 print(f'{self.nome} não está dormindo')
#         else:
#             print(f'{self.nome} está ocupado {self.acao}')
#
#     def falar(self, ordem, alvo = ""):
#         if self.acao == '':
#             print(f'{self.nome} diz {ordem}, {alvo}')
#         else:
#             print(f'{self.nome} está ocupado {self.acao}')

# class Pessoa():
#
#     def __init__(self, nome, peso, idade, comendo=False, dormindo=False, falando=False):
#         self.nome = nome
#         self.peso = peso
#         self.idade = idade
#         self.comendo = comendo
#         self.dormindo = dormindo
#         self.falando = falando
#
#     def comer(self, comida=""):
#         if self.comendo:
#             print(f'{self.nome} está ocupado comendo')
#         else:
#             self.comendo = False
#             if comida == "":
#                 print(f'{self.nome} não foi comer')
#             else:
#                 print(f'{self.nome} foi comer {comida}')
#
#     def pararComer(self):
#         if self.comendo:
#             print("João parou de comer")
#             self.comendo = False
#         else:
#             print(f'{self.nome} não está comendo')
#
#     def dormir(self, bool=True):
#         if self.dormindo:
#             if bool:
#                 self.acao = 'dormindo'
#                 print(f'{self.nome} está dormindo')
#             else:
#                 print(f'{self.nome} não está dormindo')
#         else:
#             print(f'{self.nome} está ocupado')
#
#     def pararDormir(self):
#         if self.dormindo:
#             print("João parou de dormir")
#             self.dormindo = False
#         else:
#             print(f'{self.nome} não está dormindo')
#
#     def falar(self, ordem, alvo=""):
#         if self.acao:
#             print(f'{self.nome} diz {ordem}, {alvo}')
#         else:
#             print(f'{self.nome} está ocupado')
#
#     def pararFalar(self):
#         if self.falando:
#             print("João parou de falar")
#             self.falando = False
#         else:
#             print(f'{self.nome} não está falando')
#

class ContaBancaria():
    def __init__(self, numeroconta, nomecliente, tipo):
        self.numeroconta = numeroconta
        self.nomecliente = nomecliente
        self.tipo = tipo
        self.saldo = 0.0
        self.status = False

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            print(
                f"Deposito realizado com sucesso!\nNome do cliente: {self.nomecliente}\nNumero da conta: {self.numeroconta}\nSaldo atual: R${self.saldo:.2f}")
        else:
            print(f"Conta inativa, impossível depositar. Ative-a primeiro.")

    def sacar(self, valor):
        if self.status:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque realizado com sucesso!\nSaldo atual: R${self.saldo:.2f}")
            else:
                print(f"Saldo insuficiente para o saque.\nSaldo atual: R${self.saldo:.2f}")
        else:
            print(f"Conta inativa, impossível sacar. Ative-a primeiro.")

    def verificarSaldo(self):
        if self.status:
            return f"Numero da conta: {self.numeroconta}\nSaldo atual: R${self.saldo:.2f}"
        return f"Conta inativa. Ative-a primeiro."

    def ativarConta(self):
        if not self.status:
            self.status = True
            print(f"Numero da conta: {self.numeroconta}\nStatus atual: Ativada")
        else:
            print("Conta já ativada.")

    def desativarConta(self):
        if self.status:
            if not self.saldo:
                self.status = False
                print(f"Numero da conta: {self.numeroconta}\nStatus atual: Desativada")
            else:
                print(f"Não é possivel desativar conta com saldo, saque-o primeiro.\nSaldo atual: R${self.saldo:.2f}")
        else:
            print("Conta já desativada")


class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

<<<<<<< HEAD
    def comer(self):
        print(f"O {self.nome} foi comer...")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
=======
    def comer(self, comida=""):
        if self.comendo:
            print(f'{self.nome} já está comendo')
        elif self.dormindo or self.falando:
            for nome_atributo, valor_atributo in self.__dict__.items():
                if valor_atributo is True:
                     print(f'{self.nome} está ocupado {nome_atributo}')
        else:
            if comida == "":
                print(f'{self.nome} não tinha nada pra comer')
            else:
                self.comendo = True
                print(f'{self.nome} foi comer {comida}')

    
    def pararComer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo')

    def dormir(self, bool=True):
        if self.dormindo:
            print(f'{self.nome} já está dormindo')
        
        elif self.falando or self.comendo:
            for nome_atributo, valor_atributo in self.__dict__.items():
                if valor_atributo is True:
                    print(f'{self.nome} está ocupado {nome_atributo}')
        else:
            if not bool:
                print(f'{self.nome} não está dormindo')
            else:
                self.dormindo = True
                print(f'{self.nome} está dormindo')
                
                
>>>>>>> bca368b69dd7a4905d633e76033f22e6837894c2

    def miar(self):
        print(f"O {self.nome} foi miando...")

<<<<<<< HEAD

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} foi latindo...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"O {self.nome} foi pulando...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mu(self):
        print(f"O {self.nome} foi muuuu...")
=======
    def falar(self, ordem, alvo=""):
        if self.falando:
            print(f'{self.nome} já está falando')
        elif self.comendo or self.dormindo:
            for nome_atributo, valor_atributo in self.__dict__.items():
                if valor_atributo is True:
                    print(f'{self.nome} está ocupado {nome_atributo}')
        else:
            self.falando = True
            print(f'{self.nome} diz {ordem}, {alvo}')
         

    def pararFalar(self):
        if self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
        else:
            print(f'{self.nome} não está falando')
>>>>>>> bca368b69dd7a4905d633e76033f22e6837894c2
