from classes import *

p1 = Pessoa("João",65, 23)
p2 = Pessoa("Maria",68, 24)

print(f'O {p1.nome} tem {p1.idade} anos e pesa {p1.peso}Kgs')
print(f'A {p2.nome} tem {p2.idade} anos e pesa {p2.peso}Kgs')

print()

p1.comer("coxinha")
p1.comer()
#
# print()
#
# p1.dormir()
# p2.dormir(False)
#
# print()
#
# p1.falar("vai comer", p2.nome)
# p2.falar("vai dormir", p1.nome)
