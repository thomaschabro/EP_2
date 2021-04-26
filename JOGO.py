# Importando necessárias para o jogo
from funções_EP2 import *
import random

# Criando Baralho
baralho = cria_baralho()

# Embaralhando o baralho
random.shuffle(baralho)

# Criando o funcionamento do jogo
cond = possui_movimentos_possiveis(baralho)
while cond:
    # Apresentando ao jogador a situação do jogo
    i = 1
    print ('')
    print ('Situação Atual do baralho')
    print ('===========================')
    for el in baralho:
        print (' {0}. {1}' .format(i, el))
        i+=1
    # Realizando a jogada da vez
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
        print('Você pode empilhar {0} sobre as seguintes cartas' .format(carta))
        print(' {0}. {1}' .format(1, baralho[indice-1]))
        print(' {0}. {1}' .format(2, baralho[indice-3]))
        jogada = input ('Digite o número da carta na qual deseja empilhar o {0} ' .format(carta))
        if jogada == 1:
            baralho = empilha(baralho, i, i-1)
        if jogada == 2:
            baralho = empilha(baralho, i, i-3)
    if not possíveis_movimentos:
        print ('Não é possível mexer esta carta')
    
            

