# DEFINE ONDE CADA JOGADOR VAI JOGAR
def jogadas(jogador1_jogada, jogador2_jogada):
    if jogador1_jogada == 1:
        jogo[0][0] = escolha_jogador1

    if jogador2_jogada == 1:
        jogo[0][0] = escolha_jogador2

    if jogador1_jogada == 2:
        jogo[0][1] = escolha_jogador1

    if jogador2_jogada == 2:
        jogo[0][1] = escolha_jogador2

    if jogador1_jogada == 3:
        jogo[0][2] = escolha_jogador1

    if jogador2_jogada == 3:
        jogo[0][2] = escolha_jogador2

    if jogador1_jogada == 4:
        jogo[1][0] = escolha_jogador1

    if jogador2_jogada == 4:
        jogo[1][0] = escolha_jogador2

    if jogador1_jogada == 5:
        jogo[1][1] = escolha_jogador1

    if jogador2_jogada == 5:
        jogo[1][1] = escolha_jogador2

    if jogador1_jogada == 6:
        jogo[1][2] = escolha_jogador1

    if jogador2_jogada == 6:
        jogo[1][2] = escolha_jogador2

    if jogador1_jogada == 7:
        jogo[2][0] = escolha_jogador1

    if jogador2_jogada == 7:
        jogo[2][0] = escolha_jogador2

    if jogador1_jogada == 8:
        jogo[2][1] = escolha_jogador1

    if jogador2_jogada == 8:
        jogo[2][1] = escolha_jogador2

    if jogador1_jogada == 9:
        jogo[2][2] = escolha_jogador1

    if jogador2_jogada == 9:
        jogo[2][2] = escolha_jogador2

# VARIAVEIS USADAS NO JOGO

vitoria_bola = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
vitoria_xis = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
jogo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogador2_jogada = 0
jogador1_jogada = 0
bola = 'O'
xis = 'X'
pontos_j1 = 0
pontos_j2 = 0
rodadas = 0
i = 0
verificador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'fim']

# CADA JOGADOR VAI INSERIR SEU NOME

jogador1 = str(input('Digite o nome do jogador 1: '))
jogador2 = str(input('Digite o nome do jogador 2: '))

# ECHOLA DO BOLA OU XIS
while True:
    escolha_jogador1 = ' '
    while escolha_jogador1 not in 'OX':
        escolha_jogador1 = str(input(f'{jogador1} escolha {bola} ou {xis} [{bola}/{xis}]: ')).strip().upper()[0]

    if escolha_jogador1 == bola:
        escolha_jogador2 = xis

    if escolha_jogador1 == xis:
        escolha_jogador2 = bola

    print(F'{"VAMOS JOGAR":^57}')
    print('-=' * 30)
    print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
          f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
          f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
    print('-=' * 30)
    print('Escolham onde vão jogar colocando os respectivos números do local escolhido.')

    # EXECUÇÃO DO JOGO, ALTERNANDO ENTRE CADA JOGADOR
    while True:
        print('-=' * 30)
        jogador1_jogada = int(input(f'Jogador {jogador1} escolha onde você vai jogar: '))
        if jogador1_jogada in verificador:
            verificador.remove(jogador1_jogada)
            jogadas(jogador1_jogada, jogador2_jogada)
        else:
            while jogador1_jogada not in verificador:
                print('Este local ja esta ocupado, insira outro valor: ')
                jogador1_jogada = int(input(f'Jogador {jogador1} escolha onde você vai jogar: '))
            if jogador1_jogada in verificador:
                verificador.remove(jogador1_jogada)
                jogadas(jogador1_jogada, jogador2_jogada)

        if len(verificador) == 1:
            rodadas += 1
            print('DEU VELHA')
            break

        # ESCOLHA DO JOGADOR 1 FOR BOLA
        if escolha_jogador1 == bola:

            # Vitoria na horizontal
            if jogo[0] == vitoria_bola[0] or jogo[1] == vitoria_bola[1] or jogo[2] == vitoria_bola[2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na vertical
            if jogo[0][0] == vitoria_bola[0][0] and jogo[1][0] == vitoria_bola[1][0] and jogo[2][0] == vitoria_bola[2][
                0] or jogo[0][1] == vitoria_bola[0][1] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][1] == \
                    vitoria_bola[2][1] or jogo[0][2] == vitoria_bola[0][2] and jogo[1][2] == vitoria_bola[1][2] and \
                    jogo[2][2] == vitoria_bola[2][2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria da diagonal
            if jogo[0][0] == vitoria_bola[0][0] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][2] == vitoria_bola[2][
                2] or jogo[0][2] == vitoria_bola[0][2] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][0] == \
                    vitoria_bola[2][0]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

        if i == 1:
            rodadas += 1
            pontos_j1 += 1
            break

        # ESCOLHA DO JOGADOR 1 FOR XIS
        if escolha_jogador1 == xis:

            # Vitoria na horizontal
            if jogo[0] == vitoria_xis[0] or jogo[1] == vitoria_xis[1] or jogo[2] == vitoria_xis[2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na vertical
            if jogo[0][0] == vitoria_xis[0][0] and jogo[1][0] == vitoria_xis[1][0] and jogo[2][0] == vitoria_xis[2][
                0] or jogo[0][1] == vitoria_xis[0][1] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][1] == \
                    vitoria_xis[2][1] or jogo[0][2] == vitoria_xis[0][2] and jogo[1][2] == vitoria_xis[1][2] and \
                    jogo[2][2] == vitoria_xis[2][2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na diagonal
            if jogo[0][0] == vitoria_xis[0][0] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][2] == vitoria_xis[2][
                2] or jogo[0][2] == vitoria_xis[0][2] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][0] == \
                    vitoria_xis[2][0]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

        if i == 1:
            rodadas += 1
            pontos_j1 += 1
            break

        print('-=' * 30)
        print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
              f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
              f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
        print('-=' * 30)

        jogador2_jogada = int(input(f'Jogador {jogador2} escolha onde você vai jogar: '))
        if jogador2_jogada in verificador:
            verificador.remove(jogador2_jogada)
            jogadas(jogador1_jogada, jogador2_jogada)
        else:
            while jogador2_jogada not in verificador:
                print('Este local ja esta ocupado, insira outro valor: ')
                jogador2_jogada = int(input(f'Jogador {jogador2} escolha onde você vai jogar: '))
            if jogador2_jogada in verificador:
                verificador.remove(jogador2_jogada)
                jogadas(jogador1_jogada, jogador2_jogada)

        # ESCOLHA DO JOGADOR 2 FOR BOLA
        if escolha_jogador2 == bola:

            # Vitoria na horizontal
            if jogo[0] == vitoria_bola[0] or jogo[1] == vitoria_bola[1] or jogo[2] == vitoria_bola[2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na vertical
            if jogo[0][0] == vitoria_bola[0][0] and jogo[1][0] == vitoria_bola[1][0] and jogo[2][0] == vitoria_bola[2][
                0] or jogo[0][1] == vitoria_bola[0][1] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][1] == \
                    vitoria_bola[2][1] or jogo[0][2] == vitoria_bola[0][2] and jogo[1][2] == vitoria_bola[1][2] and \
                    jogo[2][2] == vitoria_bola[2][2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria da diagonal
            if jogo[0][0] == vitoria_bola[0][0] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][2] == vitoria_bola[2][
                2] or jogo[0][2] == vitoria_bola[0][2] and jogo[1][1] == vitoria_bola[1][1] and jogo[2][0] == \
                    vitoria_bola[2][0]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

        if i == 1:
            rodadas += 1
            pontos_j2 += 1
            break

        # ESCOLHA DO JOGADOR 2 FOR XIS
        if escolha_jogador2 == xis:

            # Vitoria na horizontal
            if jogo[0] == vitoria_xis[0] or jogo[1] == vitoria_xis[1] or jogo[2] == vitoria_xis[2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na vertical
            if jogo[0][0] == vitoria_xis[0][0] and jogo[1][0] == vitoria_xis[1][0] and jogo[2][0] == vitoria_xis[2][
                0] or jogo[0][1] == vitoria_xis[0][1] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][1] == \
                    vitoria_xis[2][1] or jogo[0][2] == vitoria_xis[0][2] and jogo[1][2] == vitoria_xis[1][2] and \
                    jogo[2][2] == vitoria_xis[2][2]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

            # Vitoria na diagonal
            if jogo[0][0] == vitoria_xis[0][0] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][2] == vitoria_xis[2][
                2] or jogo[0][2] == vitoria_xis[0][2] and jogo[1][1] == vitoria_xis[1][1] and jogo[2][0] == \
                    vitoria_xis[2][0]:
                print('-=' * 30)
                print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
                      f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
                      f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
                print('-=' * 30)
                print('Você venceu')
                i += 1

        if i == 1:
            rodadas += 1
            pontos_j2 += 1
            break

        print('-=' * 30)
        print(f'{jogo[0][0]:>27}|{jogo[0][1]}|{jogo[0][2]}\n'
              f'{jogo[1][0]:>27}|{jogo[1][1]}|{jogo[1][2]}\n'
              f'{jogo[2][0]:>27}|{jogo[2][1]}|{jogo[2][2]}')
        print('-=' * 30)

    # EM CASO DE VITORIA, VOCÊ TEM A ESCOLHA DE CONTINUAR JONGANDO
    if i == 1:
        print('-=' * 30)
        print(f'RODADAS = {rodadas}')
        print('-=' * 30)
        print(f'{jogador1} = {pontos_j1} pts || {jogador2} = {pontos_j2} pts')
        print('-=' * 30)
        print('Vocês desejam continuar?')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Digite sim [S] ou não [N]: ')).strip().upper()[0]

        if continuar == 'N':
            break

        else:
            i -= 1
            jogador1_jogada = 0
            jogador2_jogada = 0
            verificador.clear()
            verificador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'fim']
            jogo.clear()
            jogo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # EM CASO DE VELHA, VOCÊ TEM A ESCOLHA DE CONTINUAR JONGANDO
    if len(verificador) == 1:
        print('-=' * 30)
        print(f'RODADAS = {rodadas}')
        print('-=' * 30)
        print(f'{jogador1} = {pontos_j1} pts || {jogador2} = {pontos_j2} pts')
        print('-=' * 30)
        print('Vocês desejam continuar?')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Digite sim [S] ou não [N]: ')).strip().upper()[0]

        if continuar == 'N':
            break

        else:
            i -= 1
            jogador1_jogada = 0
            jogador2_jogada = 0
            verificador.clear()
            verificador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'fim']
            jogo.clear()
            jogo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('Fim do jogo')