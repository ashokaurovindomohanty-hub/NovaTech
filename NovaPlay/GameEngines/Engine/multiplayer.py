class Multiplayer:
    def __init__(self):
        self.players = {}
    def join(self, pid, data):
        self.players[pid] = data
    def leave(self, pid):
        self.players.pop(pid, None)
    def sync(self):
        return self.players
