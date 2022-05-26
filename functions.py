def ler_arquivo(arquivo, jogo, game):
    with open(arquivo) as log:
        for line in log:
            if 'InitGame' in line:
                game += 1
                jogo[game] = dict()
                jogo[game]['Status'] = dict()
                jogo[game]['Status']['Total_de_kills'] = 0
                jogo[game]['Status']['Players'] = dict()
            elif 'ClientUserinfo' in line:
                a = line.strip().split()
