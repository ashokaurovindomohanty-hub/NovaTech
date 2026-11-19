class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
    def update(self, points=1):
        self.score += points
        self.high_score = max(self.score, self.high_score)
    def draw(self, screen):
        pass
    def reset(self):
        self.score = 0
