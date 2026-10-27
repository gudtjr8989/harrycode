class Food():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def print_info(self):
        print(self.name,self.price)

class Drink(Food):
    def __init__(self,name,price,volume):
        super().__init__(name,price)
        self.volume = volume
    def print_info(self):
        print(self.name,self.price,self.volume)

class Alcohol(Drink):
    def __init__(self,name,price,volume,alc_cont):
        super().__init__(name,price,volume)
        self.alc_cont=alc_cont

    def print_info(self):
        print(self.name, self.price, self.volume,self.alc_cont)







