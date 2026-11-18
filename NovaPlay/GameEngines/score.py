class Score:
    def __init__(self):
        self.score = 0

    def update(self):
        self.score += 1  # increase score every second
        print(f"Score: {self.score}")
