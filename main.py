from functions import ler_arquivo
import json

filename = 'Quake.txt'

game = 0
jogo = dict()

ler_arquivo(filename, jogo, game)

print(jogo)
