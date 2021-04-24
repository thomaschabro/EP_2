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

def extrai_naipe (carta):
    n = len(carta)
    naipe = carta[n-1]
    return naipe