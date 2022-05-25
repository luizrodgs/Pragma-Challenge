filename = 'Quake.txt'

game = 0

jogo = dict()

with open(filename) as log:
    for line in log:
        if 'InitGame' in line:
            game += 1
            jogo[game] = dict()
        else:
            a = line.strip().split(sep=' ')
            break

print(a)
