import os 

class Jogo():
    def __init__(self):
        self.a1 = " "
        self.a2 = " "
        self.a3 = " "
        self.b1 = " "
        self.b2 = " "
        self.b3 = " "
        self.c1 = " "
        self.c2 = " "
        self.c3 = " "
        self.jogadas = 0
        self.turno = 1

    def verificarGanhador(self, p):
        vence = [
            "a1a2a3",
            "b1b2b3",
            "c1c2c3",
            "a1b1c1",
            "a2b2c2",
            "a3b3c3",
            "a1b2c3",
            "c1b2a3"
        ]
        li = p.lista
        print(li)
        for i in li:
            if i in vence:
                print(f"Jogador {p.nome} ganhou!")
            else:
                print("burfro")
            

    
        
        
        
        
                        

    def mostrar(self):
        os.system('clear')
        self.guia()
        print(f"Turno: {self.turno}")
        print(f"\n {self.a1} | {self.a2} | {self.a3} \n___|___|___\n {self.b1} | {self.b2} | {self.b3} \n___|___|___\n {self.c1} | {self.c2} | {self.c3} \n")

    def guia(self):
        print(f"\n a1 | a2 | a3 \n____|____|____\n b1 | b2 | b3 \n____|____|____\n c1 | c2 | c3 \n")

class Jogador():
    def __init__(self, nome, n):
        self.nome = nome
        self.n = n
        self.pontos = 0
        self.vencedor = False
        self.jogadas = 0
        self.lista = ""

    def jogar(self, jogo, lugar):
        print("jogadas totais: ", jogo.jogadas)
        posi = getattr(jogo, lugar)
        if self.jogadas > (jogo.jogadas / 2):
            print("Não é você agora! ")
        else:
            if posi != " ":
                print(f"Já jogaram ai, jogador {self.n}")
            else:
                if self.n == 1:
                    setattr(jogo, lugar, "X")
                    self.jogadas += 1
                    jogo.jogadas += 1
                    self.lista += lugar
                    
                elif self.n == 2:
                    setattr(jogo, lugar, "O")
                    self.jogadas += 1
                    jogo.jogadas += 1
                    self.lista += lugar
            jogo.mostrar()
            print(self.lista)
            if jogo.jogadas == 9 or self.vencedor:
                print("Fim desse jogo")