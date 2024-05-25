from classes import *

jogo = Jogo()
jogo.mostrar()

p1 = Jogador((input("Digite o nome do player 1: ")), 1)
p2 = Jogador((input("Digite o nome do player 2: ")), 2)

while jogo.jogadas != 9:
  print('Jogadas: ', jogo.jogadas)
  if p1.vencedor or p2.vencedor:
    break
  elif jogo.jogadas < 9:
    j1 = input(f"{p1.nome}, digite a posição: ")
    p1.jogar(jogo, j1)
    jogo.verificarGanhador(p1)
    if jogo.jogadas < 9:
      j2 = input(f"{p2.nome}, digite a posição: ")
      p2.jogar(jogo, j2)
      jogo.verificarGanhador(p2)
      jogo.turno += 1
  else: 
    print("Deu velha!")
    
  

# jogo.jogar(1, "b1")
# jogo.mostrar()
# jogo.jogar(2, "b1")
# jogo.jogar(2, "b2")
# jogo.mostrar()
# jogo.jogar(1, "a1")
# jogo.jogar(2, "a3")
# jogo.jogar(2, "c1")



