def import_check():
    print("character_bio")

class stat:
    def __init__(self, hp, defense, atk,spd):
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.spd = spd
    def __str__(self):
        return [{self.hp},{self.defense},{self.atk},{self.spd}]

