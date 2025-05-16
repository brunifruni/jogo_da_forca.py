import desenhos as d
import fileHandler as fH
from random import choice

def jogar():
    lista_palavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras..txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)


    for x in range(50):
        print() #organiza a tela

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando?')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        #condição de vitoria
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break

        #tentativas
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou esta letra!')
            continue
        else:
            digitadas += tentativa ##ou append
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')

        score = d.desenhar_forca(erros)

        #condição de fim de jogo
        if erros == 6:
            print('ENFORCADO!')
            print(f'A palavra correta era{palavra_sorteada}.')
            break

    fH.inserir_score('score.txt', nome, score)