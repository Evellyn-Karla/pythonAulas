from classes import *




jogo = Jogo()
jogo.mostrar()

p1 = Jogador(1)
p2 = Jogador(2)
p1.jogar(jogo, "b1")
p2.jogar(jogo, "b2")
p1.jogar(jogo, "b3")
p2.jogar(jogo, "c3")
p1.jogar(jogo, "a1")
p2.jogar(jogo, "a3")
p1.jogar(jogo, "c1")


# jogo.jogar(1, "b1")
# jogo.mostrar()
# jogo.jogar(2, "b1")
# jogo.jogar(2, "b2")
# jogo.mostrar()
# jogo.jogar(1, "a1")
# jogo.jogar(2, "a3")
# jogo.jogar(2, "c1")



