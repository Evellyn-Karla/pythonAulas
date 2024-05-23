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

    def mostrar(self):
        print("Turno: 1")
        print(f"\n {self.a1} | {self.a2} | {self.a3} \n___|___|___\n {self.b1} | {self.b2} | {self.b3} \n___|___|___\n {self.c1} | {self.c2} | {self.c3} \n")

    def guia(self):
        print(f"\n ai | a2 | a3 \n___|___|___\n b1 | b2 | b3 \n___|___|___\n c1 | c2 | c3 \n")

    def verificarGanhador(self):
        p1, p2 = 0, 0
        for nome, valor in self.__dict__.items():
            if valor == "X":
                p1 += 1
            elif valor == "O":
                p2 += 1

class Jogador():
    def __init__(self, n):
        self.n = n
        self.pontos = 0
        self.jogadas = 0

    def jogar(self, jogo, lugar):
        print("jogadas totais: ", jogo.jogadas)
        posi = getattr(jogo, lugar)
        if self.jogadas > (jogo.jogadas / 2):
            print("Não é você agora! ")

        else:
            if posi == " ":
                if self.n == 1:
                    setattr(jogo, lugar, "X")
                    self.jogadas += 1
                    jogo.jogadas += 1
                elif self.n == 2:
                    setattr(jogo, lugar, "O")
                    self.jogadas += 1
                    jogo.jogadas += 1
            else:
                print(f"Já jogaram ai, jogador {self.n}")
            jogo.mostrar()
            if jogo.jogadas == 9:
                print("Fim desse jogo")