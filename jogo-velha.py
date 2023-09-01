import random
def imprimeMenuPrincipal():
    print("----------- JOGO DA VELHA -----------------")
    print("Olá jogador, vamos escolher qual modalidade você quer jogar!")
    print('-' * 50)
    print("1 - Jogador X jogador")
    print("2 - Jogador-usuário X máquina - nível fácil")
    print("3 - Jogador-usuário X máquina - nível difícil")
    print("4 - Sair")
    modo = int(input("Qual sua escolha 1, 2, 3 ou 4? "))
    return modo

def inicializarTabuleiro():
    tabuleiro = [[' ' for linha in range(3)]
                 for coluna in range(3)]
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            print(tabuleiro[linha][coluna], end=' ')
            if coluna < 2:
                print('|', end=' ')
        print()
        if linha < 2:
            print('-' * 13)

def leiaCoordenadaLinha():
    linha = int(input("Qual linha você quer marcar (1, 2 ou 3): ")) - 1
    return linha

def leiaCoordenadaColuna():
    coluna = int(input("Qual coluna você quer marcar (1, 2 ou 3): ")) - 1
    return coluna

def posicaoValida(tabuleiro, linha, coluna):
    if (0 <= linha < 3) and (0 <= coluna < 3):
        if tabuleiro[linha][coluna] == ' ':
            return True
    return False

def jogar(simbolo, tabuleiro, linha, coluna):
    if posicaoValida(tabuleiro, linha, coluna) == True:
        tabuleiro[linha][coluna] = simbolo
    else:
        print("Posição inválida")

def jogadaUsuario(tabuleiro):
    while True:
        linha = leiaCoordenadaLinha()
        coluna = leiaCoordenadaColuna()
        if posicaoValida(tabuleiro, linha, coluna):
            jogar('X', tabuleiro, linha, coluna)
            break
        else:
            print("Posição inválida. Escolha outra posição.")

def jogadaMaquinaFacil(tabuleiro):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicaoValida(tabuleiro, linha, coluna):
            jogar('O', tabuleiro, linha, coluna)
            break

def verificarVencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != ' ':
            return linha[0]

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != ' ':
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

def verificarVelha(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == ' ':
                return False
    return True

def modoJogadorVsJogador():
    print("Você está no modo jogador vs jogador, bora lá")
    pontos_jogador = 0
    pontos_jogador2 = 0
    jogador = 'X'
    jogador2 = 'O'

    while pontos_jogador < 3 and pontos_jogador2 < 3:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = jogador

        while True:
            imprimirTabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual}, é sua vez.")
            linha = leiaCoordenadaLinha()
            coluna = leiaCoordenadaColuna()

            if posicaoValida(tabuleiro, linha, coluna):
                jogar(jogador_atual, tabuleiro, linha, coluna)
                vencedor = verificarVencedor(tabuleiro)
                if vencedor:
                    imprimirTabuleiro(tabuleiro)
                    print(f"O jogador {vencedor} venceu!")
                    if vencedor == jogador:
                        pontos_jogador += 1
                    else:
                        pontos_jogador2 += 1
                    imprimirPontuacao(pontos_jogador, pontos_jogador2)
                    break
                if verificarVelha(tabuleiro):
                    imprimirTabuleiro(tabuleiro)
                    print("Deu velha!")
                    break

                if jogador_atual == jogador2:
                    jogador_atual = jogador
                else:
                    jogador_atual = jogador2
            else:
                print("Posição inválida. Escolha outra posição.")

    if pontos_jogador == 3:
        print(f"Parabéns jogador 1, você venceu o jogo!")
    elif pontos_jogador2 == 3:
        print(f"Parabéns jogador 2, você venceu o jogo!")

def modoFacil():
    print("Você está no modo jogador vs máquina, bora lá")
    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 3 and pontos_maquina < 3:
        tabuleiro = inicializarTabuleiro()
        imprimirTabuleiro(tabuleiro)

        while True:
            jogadaUsuario(tabuleiro)
            vencedor = verificarVencedor(tabuleiro)

            if vencedor:
                imprimirTabuleiro(tabuleiro)
                print(f"O jogador {vencedor} venceu!")
                pontos_jogador += 1
                imprimirPontuacao(pontos_jogador, pontos_maquina)
                break

            if verificarVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Deu velha!")
                break

            jogadaMaquinaFacil(tabuleiro)
            vencedor = verificarVencedor(tabuleiro)

            if vencedor:
                imprimirTabuleiro(tabuleiro)
                print(f"O jogador {vencedor} venceu!")
                pontos_maquina += 1
                imprimirPontuacao(pontos_jogador, pontos_maquina)
                break

            if verificarVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Deu velha!")
                break
            imprimirTabuleiro(tabuleiro)
    if pontos_jogador == 3:
        print(f"Jogador 1  venceu o jogo!")
    elif pontos_maquina == 3:
        print(f"Jogador 2  venceu o jogo!")

def jogadaMaquinaDificil(tabuleiro, jogador):
    # Aqui verifica se o jogador está prestes a ganhar em alguma linha
    for linha in range(3):
        linhaJogador = tabuleiro[linha].count(jogador)
        linhaVazia = tabuleiro[linha].count(' ')
        if linhaJogador == 2 and linhaVazia == 1:
            coluna = tabuleiro[linha].index(' ')
            tabuleiro[linha][coluna] = 'O'
            return

    # Verifica se o jogador está prestes a vencer em alguma coluna
    for coluna in range(3):
        colunaJogador = [tabuleiro[linha][coluna] for linha in range(3)].count(jogador)
        colunaVazia = [tabuleiro[linha][coluna] for linha in range(3)].count(' ')
        if colunaJogador == 2 and colunaVazia == 1:
            linha = [tabuleiro[linha][coluna] for linha in range(3)].index(' ')
            tabuleiro[linha][coluna] = 'O'
            return

    # Verifica se o jogador irá vencer na diagonal
    diagonal_jogador = [tabuleiro[i][i] for i in range(3)].count(jogador)
    diagonal_vazia = [tabuleiro[i][i] for i in range(3)].count(' ')

    if diagonal_jogador == 2 and diagonal_vazia == 1:
        linha = [tabuleiro[i][i] for i in range(3)].index(' ')
        tabuleiro[linha][linha] = 'O'
        return

    # Verifica a diagonal secundária
    diagonal2_jogador = [tabuleiro[i][2 - i] for i in range(3)].count(jogador)
    diagonal2_vazia = [tabuleiro[i][2 - i] for i in range(3)].count(' ')

    if diagonal2_jogador == 2 and diagonal2_vazia == 1:
        linha = [tabuleiro[i][2 - i] for i in range(3)].index(' ')
        tabuleiro[linha][2 - linha] = 'O'
        return

    # Se não houver jogada para bloquear, vai jogar aleatório
    jogadaMaquinaFacil(tabuleiro)

#função para o modo dificil
def modoJogadorVsMaquinaDificil():
    print("Modo jogador vs máquina - nível difícil, boa sorte :)")
    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 3 and pontos_maquina < 3:
        tabuleiro = inicializarTabuleiro()
        imprimirTabuleiro(tabuleiro)

        while True:
            jogadaUsuario(tabuleiro)
            vencedor = verificarVencedor(tabuleiro)

            if vencedor:
                imprimirTabuleiro(tabuleiro)
                print(f"O jogador {vencedor} venceu!")
                pontos_jogador += 1
                imprimirPontuacao(pontos_jogador, pontos_maquina)
                break

            if verificarVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Deu velha!")
                break

            jogadaMaquinaDificil(tabuleiro, 'X')
            vencedor = verificarVencedor(tabuleiro)

            if vencedor:
                imprimirTabuleiro(tabuleiro)
                print(f"O jogador {vencedor} venceu!")
                pontos_maquina += 1
                imprimirPontuacao(pontos_jogador, pontos_maquina)
                break

            if verificarVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Deu velha!")
                break
            imprimirTabuleiro(tabuleiro)

    if pontos_jogador == 3:
        print(f"Jogador venceu o jogo!")
    elif pontos_maquina == 3:
        print(f"Máquina venceu o jogo!")

def imprimirPontuacao(pontos_jogador, pontos_jogador2, pontos_maquina=None):
    if pontos_maquina is not None:
        print(f"Pontuação - Jogador 1 : {pontos_jogador}  Máquina: {pontos_maquina}")
    else:
        print(f"Pontuação - Jogador 1 : {pontos_jogador}  Jogador 2: {pontos_jogador2}")

# Programa Principal
while True:
    modo = imprimeMenuPrincipal()

    if modo == 1:
        modoJogadorVsJogador()
    elif modo == 2:
        modoFacil()
    elif modo == 3:
        modoJogadorVsMaquinaDificil()
    elif modo == 4:
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Tente novamente.")