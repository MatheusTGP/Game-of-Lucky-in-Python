# Jogo no Modo: MultiJogador
import time, random
print("========[ Menu Inicial ]========")
print(" Voce esta jogando no modo: MultiJogador ")
time.sleep(2)
print("Digite o nome dos dois jogadores que ira participar do game")
time.sleep(1)
player1 = input("Nome do Jogador 1: ")
player2 = input("Nome do Jogador 2: ")
time.sleep(2)
print("Todos os nomes foram salvos com sucesso!")
time.sleep(1)
print("Vamos Iniciar seu Game...")
while True:
    print("Digite um valor de 1 ~ 10, os dois players teram a possibilidade de sortear um numero")
    time.sleep(2)
    valor1 = input("Valor do Jogador 1: ")
    valor2 = input("Valor do Jogador 2: ")
    maquina  = random.randint(1, 10)
    time.sleep(2)
    print("O Ganhador do acerto foi..")
    time.sleep(2)
    if valor1 == maquina:
        print("{} Pensou em: {} \n {} Pensou em: {} \n maquina Pensou em: {}".format(player1, valor1, player2, valor2, maquina))
        print("O Jogador {} venceu a rodada".format(player1))
    else:
        print("O Jogador {} nao fez nenhum acerto correto".format(player1))
    if valor2 == maquina:
        print("O Jogador {} venceu a rodada".format(player2))
    else:
        print("O Jogador {} tambem nao fez nenhum acerto".format(player2))
