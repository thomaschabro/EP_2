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