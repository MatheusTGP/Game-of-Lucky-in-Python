# @Autor: MatheusTGamerPro
# Copyright © MatheusTGP
# Jogo no Modo: Solo
import time,random
print("========[ MiniGame in Python ]========")
time.sleep(1)
print('Ola Jogador! Vamos iniciar seu Jogo')
print('Modo de Jogo: Solo')
time.sleep(1)
player1 = input('Player1: ')
time.sleep(1)
print('Iniciando seu Jogo... \n Jogador: {}'.format(player1))
while True:
    chute1 = int(input('Digite um Valor de 1 ~ 10: '))
    máquina = random.randint(1,10)
    time.sleep(2)
    print(' Ganhador... ')
    time.sleep(1)
    if chute1 == máquina:
    	print(" {} Pensou em: {} \n máquina Pensou em: {} \n Ganhador do Jogo: {} ".format(player1, chute1, máquina, player1))
    else:
    	print('{} Pensou em: {} \n Máquina Pensou em: {} \n Ganhador do Jogo: {}'.format(player1, chute1, máquina, máquina))
