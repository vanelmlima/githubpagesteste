from time import sleep
# Variáveis
nivel = 0
rodada = [] # Lista contendo a sequência de vezes em uma rodada
# Cada item da lista será um valor booleano indicando se é a vez do jogador (True) ou do sistema (False)
vez_do_jogador = False
frase_padrao:str = 'um pato na lagoa'
boas_vindas:str = f'Vamos jogar "{frase_padrao}"'
numeros = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez']
sequencia_atual = []
continua_jogo = True


# A classe pricipal vai se chamar JogoDasFrases, permitindo que sejam criadas subclasses com os 
class Frases:
    def __init__(self, frase:str):
    
        self.frase = frase

    def criando_sequencia(self, nivel:int):
        sequencia = []
        palavras = self.frase.lower().split(' ')

        if nivel > 1:    
                palavras[0] = numeros [nivel]
                palavras[1] = palavras[1]+'s'

        for palavra in palavras:
            sequencia.extend([palavra]*nivel)
        #print(f'Sua lista de palavras é {palavras}')
        #print(f'A sequência correta desse nível é \n{sequencia}')
        nova_frase = ' '.join(palavras)
        print(f'ATENÇÃO!!! A frase é: {nova_frase}')
        return sequencia
    

umPatoNaLagoa = Frases(frase_padrao.lower())

# Método troca_vez() para chamá-lo mais facilmente ao criar a rodada
def troca(item):
    if item:
        item = False
    else:
        item = True
    return item

def verifica_resposta(inserida, correta):
    if inserida == correta:
        resposta = True
    else:
        resposta = False
        print(f'A palavra correta era "{correta}"')
    return resposta


# Para cada palavra na sequência de nível adicionar à lista rodada a vez do jogador e troca a vez até criar a lista 'rodada' com o tamanho da sequência atual
def nova_rodada(jogadas, vez):
    rodada = []
    for i in range(jogadas):

        rodada.append(vez)
        vez = troca(vez)
    return rodada

# Início do programa: 
# jogando():

print(boas_vindas)
primeiro = input('Quer ser o primeiro?\n[0] Sim ou \n[1] Não\n')


if primeiro == '0':
    print('Perfeito! Pode começar')
    vez_do_jogador = True
else:
    print('Certo, então eu começo.')
    vez_do_jogador = False

# Iniciando a primeira rodada

while continua_jogo:
    # Iniciando novo nível:
    nivel += 1
    sleep(0.5)

    print(f'Nível: {nivel}')    
    
    # Criando lista com a sequencia correta da rodada (sequencia_do_nivel) para ser comparada com a sequencia_atual
    sequencia_do_nivel = umPatoNaLagoa.criando_sequencia(nivel)
    n_jogadas = len(sequencia_do_nivel) * nivel
    # Criando rodada
    rodada = nova_rodada(n_jogadas, vez_do_jogador)
    #print(f'A rodada atual é \n{rodada}')

    # Para cada posição dos elementos de 'rodada' a variável 'palavra' recebe a palavra da jogada usando o método jogada(rodada[i], i) 
    # Sendo o primeiro parâmetro o elemento (True ou False) que define se é a vez do jogador ou do sistema
    # E o segundo parâmetro o índice do elemento na lista 'rodada' que é usado para obter a palavra na lista sequência_do_nível quando for a vez do sistema

    # Criando um método jogada para adicionar à lista a palavra da jogada de acordo com a vez
    
    for i in range(len(sequencia_do_nivel),):
        sua_vez = rodada[i]
        certa = sequencia_do_nivel[i]
        if sua_vez == True:
            print('Sua vez: ')
            palavra = str(input('* ')).lower()
        else:
            print('Minha vez...')
            sleep(1)
            palavra = certa
            print(f'** {palavra}')

        sequencia_atual.append(palavra)
        continua_jogo = verifica_resposta(palavra, certa)
        if continua_jogo == False:
            break
        
    sequencia_atual = []
    if continua_jogo:
        print('Parabéns! Você passou de nível')

# Fora do loop quando o jogador perde:
if nivel <= 10:
    print(f'Você perdeu! \nVocê conseguiu chegar até o nível {nivel}\nO JOGO')
else:
    print(f'CHEGA DE PATOS NA LAGOA \nP A RA B É N S! Você ganhou mas... \nperdeu seu tempo \n e O JOGO')
