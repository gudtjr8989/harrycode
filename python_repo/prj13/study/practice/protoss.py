def import_check():
    print("protoss was successfully imported")

class unit_stat:
    def __init__(self,name,hp,mp,atk,defs):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defs = defs
    def __str__(self):
        return f"{self.name} {self.hp} {self.mp} {self.atk} {self.defs}"
    def __list__(self):
        return [self.name, self.hp, self.mp, self.atk, self.defs]
