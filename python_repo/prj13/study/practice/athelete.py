def import_check():
    print("athelete import success")

class Athelete():
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return f"{self.name} {self.age} {self.height} {self.weight}"

    def eat(self):
        print("쳐묵 쳐묵")


