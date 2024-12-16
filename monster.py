class Monster:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = 50 + (level * 10)
        self.attack = 5 + (level * 2)
        self.defense = 3 + level

def create_goblin(level=1):
    return Monster("Gobelin", level)

def create_dragon():
    return Monster("Dragon", level=10)
