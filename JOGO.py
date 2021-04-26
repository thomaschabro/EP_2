# Importando necessárias para o jogo
from funções_EP2 import *
import random

# Criando Baralho
baralho = cria_baralho()

# Embaralhando o baralho
random.shuffle(baralho)

# Inicialização do jogo, apresentando as regras
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print ('')
print ('==========================================================')
print (color.BOLD + 'Bem vindo ao Paciência Acordeão!' + color.END)
print ('Regras:')
print ('O seu objetivo neste jogo é empilhar cartas, até sobrar apenas uma única pilha')
print ('')
print ('')
print ("Existem apenas dois movimentos possíveis:")
print ('')
print (' 1. Empilhar uma carta sobre a carta imediatamente anterior;')
print (" 2. Empilhar uma carta sobre a terceira carta anterior.") 
print ('')
print ('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')
print ('')
print (' 1. As duas cartas possuem o mesmo valor ou ')
print (' 2. As duas cartas possuem o mesmo naipe. ')
print ('')
print ('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')

# Criando o funcionamento do jogo
Jogar = True
while Jogar:
    cond = possui_movimentos_possiveis(baralho)
    while cond:
        # Apresentando ao jogador a situação do jogo
        i = 1
        print ('')
        print ('===========================')
        print ('Situação Atual do seu baralho')
        # Aplicando cor às cartas do baralho
        for el in baralho:
            if extrai_naipe(el) == '♠':
                print (' {0}. {1} \033[0;0m'.format(i,'\033[96m' + el)) 
            if extrai_naipe(el) == '♥':
                print (' {0}. {1} \033[0;0m'.format(i,'\033[91m' + el)) 
            if extrai_naipe(el) == '♦':
                print (' {0}. {1} \033[0;0m'.format(i,'\033[93m' + el)) 
            if extrai_naipe(el) == '♣':
                print (' {0}. {1} \033[0;0m'.format(i,'\033[92m' + el)) 
            i+=1
        # Realizando a jogada da vez
        indice = int(input('Digite a posição da carta que deseja mover ({0} - {1}) ' .format(1, len(baralho))))
        while indice < 1 or indice > len(baralho):
            print ('Número inválido. Digite um número entre 1 e {0}' .format(len(baralho)))
            indice = int(input('Digite a posição da carta que deseja mover ({0} - {1}) ' .format(1, len(baralho))))
        indice -= 1
        carta = baralho[indice]
        possíveis_movimentos = lista_possiveis_movimentos(baralho, indice)
        if len(possíveis_movimentos) == 1:
            if possíveis_movimentos[0] == 1:
                baralho = empilha(baralho, indice, indice -1)
            if possíveis_movimentos[0] == 3:
                baralho = empilha(baralho, indice, indice-3)
        if len(possíveis_movimentos) == 2:
            naipe = extrai_naipe(carta)
            if naipe == '♠':
                print('Você pode empilhar {0} \033[0;0m' .format('\033[96m' + carta) + 'sobre as seguintes cartas')
            if naipe == '♥':
                print('Você pode empilhar {0} \033[0;0m' .format('\033[91m' + carta) + 'sobre as seguintes cartas')
            if naipe == '♦':
                print('Você pode empilhar {0} \033[0;0m' .format('\033[93m' + carta) + 'sobre as seguintes cartas')
            if naipe == '♣':
                print('Você pode empilhar {0} \033[0;0m' .format('\033[92m' + carta) + 'sobre as seguintes cartas')
            naipe_1 = extrai_naipe(baralho[indice-1])
            if naipe_1 == '♠':
                print(' {0}. {1}\033[0;0m' .format(1, '\033[96m' + baralho[indice-1])) 
            if naipe_1 == '♥':
                print(' {0}. {1}\033[0;0m' .format(1, '\033[91m' + baralho[indice-1]))
            if naipe_1 == '♦':
                print(' {0}. {1}\033[0;0m' .format(1, '\033[93m' + baralho[indice-1]))
            if naipe_1 == '♣':
                print(' {0}. {1}\033[0;0m' .format(1, '\033[92m' + baralho[indice-1]))
            naipe_3 = extrai_naipe(baralho[indice-3])
            if naipe_3 == '♠':
                print(' {0}. {1}\033[0;0m' .format(2, '\033[96m' + baralho[indice-3])) 
            if naipe_3 == '♥':
                print(' {0}. {1}\033[0;0m' .format(2, '\033[91m' + baralho[indice-3]))
            if naipe_3 == '♦':
                print(' {0}. {1}\033[0;0m' .format(2, '\033[93m' + baralho[indice-3]))
            if naipe_3 == '♣':
                print(' {0}. {1}\033[0;0m' .format(2, '\033[92m' + baralho[indice-3]))
            jogada = int(input ('Digite o número escolhido '))
            while jogada != 1 and jogada != 2:
                print ('Número inválido. Escolha entre a opção 1 e a opção 2')
                jogada = int(input ('Digite o número escolhido '))
            if jogada == 1:
                baralho = empilha(baralho, indice, indice-1)
            if jogada == 2:
                baralho = empilha(baralho, indice, indice-3)
        if not possíveis_movimentos:
            print ('Não é possível mexer esta carta')
    if len(baralho) > 1:
        print ('Parabéns, você ganhou!')
    if len(baralho) != 1:
        print ('Infelizmente, você não deu sorte dessa vez. Tente outra vez!')   
    repetição = input ('Você deseja jogar novamente?')
    if repetição == 'sim':
        Jogar = True
    if repetição == 'não':
        Jogar = False


