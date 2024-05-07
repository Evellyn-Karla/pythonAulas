
# meu codigo foi feito no replit, pode ser necessário algumas alterações dependendo da versao do python

''' Exercício 08

Faça um código para ler 5 nomes de 

usuários e suas respectivas senhas, e 

armazenar cada lista em um array 

diferente, após completar a digitação, 

imprimir , nome, senha e posição dos 

dados no array '''



'''criando uma função pra rodar cada exercício'''
def ex08():

  '''criando os vetores para o exercicio'''
  nomes = ["", "", "", "", ""]
  senhas = ["", "", "", "", ""]

  '''loop para preencher cada indice dos vetores com input do usuário '''
  for i in range(len(nomes)):
    nomes[i] = input("Digite o nome: ")
    senhas[i] = input("Digite a senha: ")

  '''loop para mostrar cada nome e senha no mesmo indice e seu indice'''
  for i in range(len(nomes)):
    print(f"Nome: {nomes[i]} - Senha: {senhas[i]} - Posição: {i}")
    

'''Exercício 09

Altere o sistema anterior e faça um sistema 

de login, pedindo a senha do usuário e 

mostrando seu nome e a mensagem, login 

efetuado com sucesso'''

def ex09():
  
  nomes = ["", "", "", "", ""]
  senhas = ["", "", "", "", ""]
  op = 0
  
  while op != 3:
    op = int(input("\n---- Sistema ----\n1-Cadastro\n2-Login\n3-Sair\n"))
    if op == 1:
      print("\n====Cadastro no sistema====")
      for i in range(len(nomes)):
        nomes[i] = input("Digite o nome: ")
        senhas[i] = input("Digite a senha: ")
  
      '''prints para mostrar que foram registrados e pedindo para logar'''
      print("Cadastro realizado com sucesso!")

    if op == 2:
      print("\n========Login=========")
      print("Digite seu nome e senha para acessar o sistema")
    
      '''nome para verificar se existe igual no vetor nomes'''
      nome = input("Digite seu nome: ")
      
      '''loop para pedir nome ate ele ser um igual aos já cadastrados'''
      while nome not in nomes:
        print("Nome não encontrado")
        nome = input("Digite seu nome: ")
    
      '''se nome existir nos nomes cadastrados, 
      verificar qual o índice com loop para percorrer a lista comparando'''
      
      for n in range(len(nomes)):
        if nome == nomes[n]:
          senha = input("Digite sua senha: ") 
          
          ''' comparar senha digitada com senha cadastrada no mesmo indice que o nome'''
          if senha == senhas[n]: 
            print(f"Acesso liberado! Bem vindo(a) {nome}.")
          else:
            print("Senha incorreta!")

  print("Xauzinhoo")


'''Exercício 10

Faça um código para ler um valor N qualquer (que 

será o tamanho dos vetores). Após, ler dois

vetores A e B (de tamanho N cada um) e depois 

armazenar em um terceiro vetor Soma a soma dos

elementos do vetor A com os do vetor B 

(respeitando as mesmas posições) e escrever o 

vetor Soma'''



def ex10():
  n = int(input("Digite o tamanho dos vetores: "))

  '''tamanho dos vetores calculados com base em n, mesma coisa que escrever a = [0, 0, 0, 0, ...] varias vezes'''
  
  a = [0] * n
  b = [0] * n
  soma = [0] * n
  
  '''loop para preencher os vetores a e b no msm indice ate preencher tudo'''
  for i in range(len(a)):
    a[i] = int(input("Digite um valor para o vetor A: "))
    b[i] = int(input("Digite um valor para o vetor B: "))

    '''no fim fica tipo assim se n for 5 a = [1,5,6,8,9], b = [2,3,4,5,6] dependendo dos valores digitados e soma fica [3,8,10,12,15]''' 
    soma[i] = a[i] + b[i]
  
  print(soma)

'''Exercício 11

Faça um código para ler um vetor de 30 

números. Após isto, ler mais um número 

qualquer, calcular e escrever quantas 

vezes esse número aparece no vetor.'''



def ex11():
  nums = [0] * 6
  total = 0

  '''loop pra preencher nums'''
  for i in range(len(nums)):
    nums[i] = int(input("Digite um número: "))

  '''pedingo pro usuário o numero pra procurar em nums'''
  n = int(input("Digite outro número: "))

  '''pra cada vez que n aparecer em nums total recebe + 1'''
  for i in range(len(nums)):
    if nums[i] == n:
      total += 1
  print(f"O número {n} aparece {total} vezes em nums.")

'''Exercício 12

Escreva um algoritmo que solicite ao 

usuário a entrada de 5 nomes, e que exiba 

a lista desses nomes na tela.

Após exibir essa lista, o programa deve 

mostrar também os nomes na ordem 

inversa em que o usuário os digitou, um 

por linha.'''

def ex12():

  '''mesma coisa que digitar nomes = ["", "",...5x]'''
  nomes = [""] * 5

  '''loop pra preencher nomes'''
  for i in range(len(nomes)):
    nomes[i] = input("Digite um nome: ")

  '''loop pra mostrar nomes do ultimo ao primeiro, ele começa em tamanho da lista nomes (5) - 1 e para de executar qnd chega em -1 '''
  
  '''se os nomes digitados forem assim ["a", "b", "c", "d", "e"] ele vai mostrar: e, d, c, b, a.  do indice 4 ao 0'''
  for i in range(len(nomes)-1, -1, -1):
    print(nomes[i])

''' Exercício 13

Faça um algoritmo que leia 30 valores do 

tipo inteiro e armazene-os em um vetor. 

A seguir, o algoritmo deverá informar 

(1) todos os números pares que existem no 

vetor; 

(2) o menor e o maior valor existente no 

vetor; 

(3) quantos dos valores do vetor são 

maiores que a média desses valores:'''

def ex13():

  '''inicializando as variaveis que sera utilizadas'''

  '''melhor fazer com um numero menor para testar pq vc vai ter que digitar muitas vezes'''
  nums = [0] * 6
  
  pares = 0
  maior = 0
  menor = 0
  soma = 0
  media = 0
  maiorM = 0

  '''loop pra preencher nums'''
  for i in range(len(nums)):
    nums[i] = int(input("Digite um número: "))

    '''somar cada numero e salvar em soma'''
    soma += nums[i]

    ''' verificar se é zero, se for igual a zero ele soma mais um a pares e volta pro inicio do loop e n executa o que vem depois '''

    '''escolhi fzr com 0 sendo par'''

    
    '''caso queira remover 0 para n ser par
    zeros = 0
    if nums[i] == 0:
      zeros += 1
      break
    e adicione - zeros no calculo de impares
    '''

    
    '''calcular o resto da divisao por 2 para saber se é par'''
    if nums[i] % 2 == 0:
      pares += 1

  '''se tirar todos os pares do total o que sobra sao os impares'''
  impares = len(nums) - pares # - zeros


  '''calculo da soma de todos dividio pela quantidade de números para obter media '''
  media = soma / len(nums)

  for i in range(len(nums)):
    '''ver quais números sao maiores que a media e salvar em maiorM'''
    if nums[i] > media:
      maiorM += 1

    '''para cada numero ver se ele é maior que o armazenado na variavel maior, se for ele maior se torna ele '''
    if nums[i] > maior:
      maior = nums[i]

    '''para menor ele verifica se o numero atual é menor que o anterior, se for ele se torna o menor'''
    if nums[i] < nums[i-1]:
      menor = nums[i]
    
  print(f"1° Existem {pares} números pares e {impares} impares no vetor.")
  print(f"2° O maior número é {maior} e o menor é {menor}.")

  '''detalhe :.1f em media para exibir um numero com só um digito depois da virgula'''
  print(f"3° A média dos números é {media:.1f} e os números maiores que a média são {maiorM}.")




''' todo o menu e criação de funçoes com def é uma coisa que eu escolhi pra facilitar as execuçoes de cada um, pode fazer sem eles que funciona igual os codigos'''


def menu():
  '''Menu de escolha de exercicios '''
  exes = {
    8: ex08,
    9: ex09,
    10: ex10,
    11: ex11,
    12: ex12,
    13: ex13
  }
  '''inicializado escolha em um numero aleatorio'''
  escolha = -1

  '''rodar enquanto escolha nao receber 0'''
  while escolha != 0:
    '''escolha do menuzinho de exercicios'''
    print('Exercicios de 08 a 13 de listas')
    escolha = int(input('Digite o exercicio (ou 0 para sair): '))

    if escolha == 0:
      break

    
    '''verifica se escolha definida esta em exes e executa caso esteja'''
    if escolha in exes:
      exes[escolha]()
    else:
      print('Exercicio não encontrado')

menu()

  

