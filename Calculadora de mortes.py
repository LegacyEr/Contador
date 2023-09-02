__author__ = "Erick de Souza Dias"
import time

def main ():
    l_jogos = ['Vazio', 'God of War', 'Elden Ring', 'Fortnite']
    Nj = len(l_jogos)
    jogos = '1 God of War\n 2 Elden Ring\n 3 Fortnite\n'
    i = 0
    I = 1
    m_1 = 0
    m_2 = 0
    m_3 = 0
    m_4 = 0
    m_5 = 0

    i0 = 0
    I0 = 1
    while i0 != I0:
        i0 += 1

        print("Mortes de NovemBrocha.\n\nEscolha o jogo no qual ele está morrendo\n", jogos, Nj, 'Adiconar outro Jogo'
                                                                                                 '\n Precione 0 para '
                                                                                                 'sair')

        while i != I:
            i += 1
            try:
                r = int(input("\nInforme o número do jogo que deseja\n"))
            except ValueError:
                print("O valor inserido precisa ser um número inteiro")
                I += 1
        #tratamento de erros

        for t in range(26):
            time.sleep(0.0000001)
            print(' ')
        #espaço

        if r == 0:
            print('\nAté mais\n Salvando dados...')

            for t in range(101):
                time.sleep(0.0000001)
                print('{}%'.format(t))
            # espaço

        elif r == 1:
            print('\n                God of War')
            print('\nO Novembrow já morreu', m_1, 'neste jogo\n\nEscolha entre\n1 se deseja adicionar mais uma morte\n'
                                                              '2 se deseja retirar uma morte do contador\n'
                                                              '3 se deseja reiniciar o contador\n4 se deseja voltar')

            i1 = 0
            I1 = 1
            while i1 != I1:
                i1 += 1
                try:
                    r2 = int(input("\nInforme o número da opção que deseja\n"))
                except ValueError:
                    print("O valor inserido precisa ser um número inteiro")
                    I1 += 1
            # Tratamento de erro de resposta

            for t in range(26):
                time.sleep(0.0000001)
                print(' ')
            # espaço

            i2 = 0
            I2 = 1
            while i2 != I2:
                i2 += 1
                if r2 == 1:
                    m_1 += 1
                    print('\n                God of War')
                    print('\nO Novembrow já morreu', m_1, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    #tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        m_1 -= 2
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_1 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                        #tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_1 -= 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 2:
                    m_1 -= 1
                    print('\n                God of War')
                    print('\nO Novembrow já morreu', m_1, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        m_1 += 2
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_1 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            #tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_1 += 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 3:
                    m_1 = 0
                    print('\n                God of War')
                    print('\nO Novembrow já morreu', m_1, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_1 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                            for t in range(26):
                                time.sleep(0.0000001)
                                print(' ')
                            # espaço

                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 4:
                    I0 += 1
                else:
                    print('\nInforme um número correspondente a opção que deseja\n')
                    I2 += 1


        elif r == 2:
            print('\n                Elden Ring')
            print('\nO Novembrow já morreu', m_2, 'neste jogo\n\nEscolha entre\n1 se deseja adicionar mais uma morte\n'
                                                  '2 se deseja retirar uma morte do contador\n'
                                                  '3 se deseja reiniciar o contador\n4 se deseja voltar')

            i1 = 0
            I1 = 1
            while i1 != I1:
                i1 += 1
                try:
                    r2 = int(input("\nInforme o número da opção que deseja\n"))
                except ValueError:
                    print("O valor inserido precisa ser um número inteiro")
                    I1 += 1
            # Tratamento de erro de resposta

            for t in range(26):
                time.sleep(0.0000001)
                print(' ')
            # espaço

            i2 = 0
            I2 = 1
            while i2 != I2:
                i2 += 1
                if r2 == 1:
                    m_2 += 1
                    print('\n                Elden Ring')
                    print('\nO Novembrow já morreu', m_2, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        m_2 -= 2
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_2 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                        # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_2 -= 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 2:
                    m_2 -= 1
                    print('\n                Elden Ring')
                    print('\nO Novembrow já morreu', m_2, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        m_2 += 2
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_2 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_2 += 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 3:
                    m_2 = 0
                    print('\n                Elden Ring')
                    print('\nO Novembrow já morreu', m_2, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_2 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 4:
                    I0 += 1
                else:
                    print('\nInforme um número correspondente a opção que deseja\n')
                    I2 += 1

        elif r == 3:
            print('\n                Fortnite')
            print('\nO Novembrow já morreu', m_3, 'neste jogo\n\nEscolha entre\n1 se deseja adicionar mais uma morte\n'
                                                  '2 se deseja retirar uma morte do contador\n'
                                                  '3 se deseja reiniciar o contador\n4 se deseja voltar')

            i1 = 0
            I1 = 1
            while i1 != I1:
                i1 += 1
                try:
                    r2 = int(input("\nInforme o número da opção que deseja\n"))
                except ValueError:
                    print("O valor inserido precisa ser um número inteiro")
                    I1 += 1
            # Tratamento de erro de resposta

            for t in range(26):
                time.sleep(0.0000001)
                print(' ')
            # espaço

            i2 = 0
            I2 = 1
            while i2 != I2:
                i2 += 1
                if r2 == 1:
                    m_3 += 1
                    print('\n                Fortnite')
                    print('\nO Novembrow já morreu', m_3, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        m_3 -= 2
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_3 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_3 -= 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 2:
                    m_3 -= 1
                    print('\n                Fortnite')
                    print('\nO Novembrow já morreu', m_3, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        m_3 += 2
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_3 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_3 += 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 3:
                    m_3 = 0
                    print('\n                Fortnite')
                    print('\nO Novembrow já morreu', m_3, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_3 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 4:
                    I0 += 1
                else:
                    print('\nInforme um número correspondente a opção que deseja\n')
                    I2 += 1

        elif r == Nj:
            print('\nok\n')
            l_jogos.append(input('\nInsira aqui o nome do jogo\n'))
            I0 += 1

        elif r == 4:
            print('\n                ', l_jogos[4])
            print('\nO Novembrow já morreu', m_4, 'neste jogo\n\nEscolha entre\n1 se deseja adicionar mais uma morte\n'
                                                  '2 se deseja retirar uma morte do contador\n'
                                                  '3 se deseja reiniciar o contador\n4 se deseja voltar')

            i1 = 0
            I1 = 1
            while i1 != I1:
                i1 += 1
                try:
                    r2 = int(input("\nInforme o número da opção que deseja\n"))
                except ValueError:
                    print("O valor inserido precisa ser um número inteiro")
                    I1 += 1
            # Tratamento de erro de resposta

            for t in range(26):
                time.sleep(0.0000001)
                print(' ')
            # espaço

            i2 = 0
            I2 = 1
            while i2 != I2:
                i2 += 1
                if r2 == 1:
                    m_4 += 1
                    print('\n                ', l_jogos[4])
                    print('\nO Novembrow já morreu', m_4, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        m_4 -= 2
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_4 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                        # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_4 -= 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 2:
                    m_4 -= 1
                    print('\n                ', l_jogos[4])
                    print('\nO Novembrow já morreu', m_4, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço


                    if r1 == 1:
                        m_4 += 2
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_4 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        m_4 += 1
                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 3:
                    m_4 = 0
                    print('\n                ', l_jogos[4])
                    print('\nO Novembrow já morreu', m_4, 'neste jogo\n\nEscolha entre\n'
                                                          '1 se deseja adicionar mais uma morte\n'
                                                          '2 se deseja retirar uma morte do contador\n'
                                                          '3 se deseja adicionar um número determinado de mortes'
                                                          '\n4 se deseja voltar')

                    i_1 = 0
                    I_1 = 1
                    while i_1 != I_1:
                        i_1 += 1
                        try:
                            r1 = int(input("\nInforme o número da opção que deseja\n"))
                        except ValueError:
                            print("O valor inserido precisa ser um número inteiro")
                            I_1 += 1
                    # tratamento de erro

                    for t in range(26):
                        time.sleep(0.0000001)
                        print(' ')
                    # espaço

                    if r1 == 1:
                        I2 += 1
                    elif r1 == 2:
                        I2 += 1
                    elif r1 == 3:
                        i3 = 0
                        I3 = 1
                        while i3 != I3:
                            i3 += 1
                            try:
                                m_4 += int(input('\nInforme o número de mortes que deseja adicionar\n'))
                            except ValueError:
                                print("O valor inserido precisa ser um número inteiro")
                                I3 += 1
                            # tratamento de erro

                        for t in range(26):
                            time.sleep(0.0000001)
                            print(' ')
                        # espaço

                        I2 += 1
                    elif r1 == 4:
                        print('\nok\n')
                        I0 += 1
                        I += 1

                    else:
                        print('Informe um número correspondende a seu desejo')
                        I2 += 1
                elif r2 == 4:
                    I0 += 1
                else:
                    print('\nInforme um número correspondente a opção que deseja\n')
                    I2 += 1

        else:
            print('Informe um número correspondende a seu desejo')

if __name__ == '__main__':
    main()



