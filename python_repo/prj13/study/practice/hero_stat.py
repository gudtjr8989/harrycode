class stat:
    def __init__(self,name,hp,mp,atk,defs,spd):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defs = defs
        self.spd = spd
    def __str__(self):
        return f"{self.name} {self.hp} {self.mp} {self.atk} {self.defs} {self.spd}"
    def __list__(self):
        return [self.name, self.hp, self.mp, self.atk, self.defs, self.spd]


