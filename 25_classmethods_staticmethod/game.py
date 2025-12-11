class Game:
    def __init__(self, title, players):
        self.title = title
        self.players = players

    def details(self):
        return f"{self.title} supports {self.players} players"

    @classmethod
    def multiplayer_version(cls, game):
        return cls(game.title, game.players + 1)

    @staticmethod
    def game_info(game):
        return f"Game: {game.title} (Players: {game.players})"    

g1 = Game("Fortnite", 1)
g2 = Game.multiplayer_version(g1)

print(g2.details())
print(Game.game_info(g1))