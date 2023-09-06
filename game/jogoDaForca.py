# bibliotecas
# array
import numpy as np

# random
from random import randint

# layout tela
from PySimpleGUI import PySimpleGUI as Sg

# Armazenador de palavras
palavras = np.array(["cachorro", "gato", "foca", "hiena", "cavalo", "pinguim"])

# Armazenador de dicas


# sortear palavra do array
def sortear_palavra(length):
    # coloca valor sorteado dentro de variável
    number = randint(0, (length - 1))

    # retorna palavra de acordo com número sorteado
    return palavras[number]


# Inicialização do game
def iniciar(palavra):
    # comparador
    contador = 0
    # layout das linhas jogo da forca
    formato = []
    qtd_caracteres = formatacao(0, palavra)
    palavra_sorteada_array = formatacao(1, palavra)

    while contador < qtd_caracteres:
        formato += '_'
        contador += 1

    # Dica e letras totais
    tela_gamer(qtd_caracteres, formato, palavra_sorteada_array)


# Separar e contar letras da palavra sorteada
def formatacao(number, string):
    # Variável armazenar array
    caract = []

    # Contador de letras
    cont = 0

    # loop de acordo com letras
    for caractere in string:
        # Recebe ele + ele mesmo
        caract += caractere

        # Contador aumenda de acordo com mais letras
        cont = cont + 1

    # Se 0 retorna apenas o contador de letras
    if number == 0:
        return cont
    # Senão retorna array
    elif number == 1:
        return caract


def jogada(array_letras_jogadas, palavra_sort, letra_jogada):
    print('sorteada {}, letra jogada {}'.format(palavra_sort, letra_jogada))
    array_l = array_letras_jogadas
    print(array_l)
    index = 0
    for letra in palavra_sort:
        if array_l == "":
            if letra == letra_jogada:
                array_l[index] = letra_jogada
            else:
                array_l[index] = '_'

            index += 1
        else:
            if letra == letra_jogada:
                array_l.append(letra_jogada)
            else:
                array_l.append('_')

    formato = ''
    for letra in array_l:
        formato += ' {} '.format(letra)

    print(array_l)
    return formato


# Visual
def tela_gamer(qtd_letras, formato_forca, p_sorteada):
    array_jogadas = []
    formato_letras_tela = ''
    tentativas = 8

    for index in formato_forca:
        formato_letras_tela += ' {} '.format(index)

    def tela_inicial(todas_jogadas, atualizacao_display, t_tela):
        letras_jogadas = todas_jogadas

        if t_tela == 0:
            formato_array_tela = formato_letras_tela
        else:
            formato_array_tela = atualizacao_display

        Sg.theme('Dark Blue 1')
        layout = [
            [Sg.Text(formato_array_tela)],
            [Sg.Text('Tem {} letras'.format(qtd_letras))],
            [Sg.Text('Dica: Animal'), Sg.Text('Tentativas: {}'.format(tentativas))],
            [Sg.Text('Letras jogadas: {}'.format(todas_jogadas.lower()))],
            [Sg.Input(key="key_letra", size=(30, 1))],
            [Sg.Button("Enviar")]
        ]
        # janela
        janela = Sg.Window("Jogo da Forca", layout)

        while True:
            eventos, valores = janela.read()
            if eventos == Sg.WINDOW_CLOSED:
                break
            if eventos == "Enviar":
                array_letras_jogadas = array_jogadas
                janela.close()
                tipo_jogada = 1
                letras_jogadas += '{}, '.format(valores['key_letra'])
                acertos = jogada(array_letras_jogadas, p_sorteada, valores['key_letra'])
                tela_inicial(letras_jogadas, acertos, tipo_jogada)

    tela_inicial('', '', 0)


# Inicia o programa
iniciar(sortear_palavra(palavras.size))
