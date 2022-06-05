class Partida:
    def __init__(self, game_id):
        self.id = game_id
        self.total_kills = 0
        self.players = []


class Player:
    def __init__(self, player_id, player_nome):
        self.id = player_id
        self.nome = player_nome
        self.kills = 0
        self.nomes_antigos = []
