# Função para criar o baralho do jogo
def cria_baralho ():
    # Definindo presets para criação do baralho
    baralho = []
    naipes = ['♠', '♥', '♦', '♣']
    # Adicionando todas as cartas de cada nipe
    for i in naipes:
        for el in range(2, 11):
            carta = str(el) + i
            baralho.append(carta)
        carta = 'J' + i
        baralho.append(carta)
        carta = 'Q' + i
        baralho.append(carta)
        carta = 'K' + i
        baralho.append(carta)
        carta = 'A' + i
        baralho.append(carta)
    return baralho

# Função para extrair o naipe da carta
def extrai_naipe (carta):
    n = len(carta)
    naipe = carta[n-1]
    return naipe

# Função para extrair o valor da carta
def extrai_valor (carta):
    n = len(carta)
    valor = ''
    i = 0
    while i < n-1:
        valor += carta[i]
        i+=1
    return valor

# Função para definir os possíveis movimentos 
def lista_possiveis_movimentos (baralho, i):
    # Definindo valor e naipe da carta do índice indicado
    carta = baralho[i]
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)
    movimentos_possiveis = []
    if i == 0:
        return movimentos_possiveis
    # Definindo valor e naipe da carta imediatamente anterior
    carta_ant = baralho[i-1]
    naipe_ant = extrai_naipe(carta_ant)
    valor_ant = extrai_valor(carta_ant)
    # Definindo valor e naipe da carta 3 posições antes
    carta_3ant = baralho[i-3]
    naipe_3ant = extrai_naipe(carta_3ant)
    valor_3ant = extrai_valor(carta_3ant)
    if i>0 and i<3:
        if naipe == naipe_ant:
            movimentos_possiveis.append(1)
        if valor == valor_ant:
            movimentos_possiveis.append(1)
    if i >= 3: 
        if naipe == naipe_ant:
            movimentos_possiveis.append(1)
        if valor == valor_ant:
            movimentos_possiveis.append(1)
        if naipe == naipe_3ant:
            movimentos_possiveis.append(3)
        if valor == valor_3ant:
            movimentos_possiveis.append(3)
    return movimentos_possiveis

# Função para empilhar as cartas
def empilha (baralho, i, f):
    baralho[f] = baralho [i]
    del baralho [i]
    return baralho

# Função para verificar se ainda existem possíveis movimentos no baralho
def possui_movimentos_possiveis (baralho):
    verif = []
    for el in baralho:
        i = baralho.index(el)
        x = lista_possiveis_movimentos(baralho, i)
        if x != []:
            return True
    return False

