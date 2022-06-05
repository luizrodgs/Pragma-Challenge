import re

from models import Partida, Player


def ler_arquivo(arquivo, partidas, id_partida, lista_partidas, lista_players):
    with open(arquivo) as log:
        for line in log:
            if "InitGame" in line:
                players_atual = []
                id_partida += 1
                Partida_atual = Partida(id_partida)
                lista_partidas.append(Partida_atual)
            elif "ClientUserinfo" in line:
                a = line.strip().split()
                player_id = a[2]
                if player_id not in players_atual:
                    players_atual.append(player_id)
                    Player_atual = Player(player_id, "nometeste")
                    lista_players.append(Player_atual)
            elif "ShutdownGame" in line:
                Partida_atual.players.append(players_atual)
                partidas.append(Partida_atual)

    for partida in partidas:
        print(partida.id, partida.players)
