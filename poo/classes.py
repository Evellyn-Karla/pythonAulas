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

class Pessoa():

    def __init__(self, nome, peso, idade, comendo = False, dormindo = False, falando = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando

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
                
                

    def pararDormir(self):
        if self.dormindo:
            print("João parou de dormir")
            self.dormindo = False
        else:
            print(f'{self.nome} não está dormindo')

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