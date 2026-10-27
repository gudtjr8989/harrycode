#method override
class Drink:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return(self.name, self.price)

    def print_info(self):
        print(f"Drink self.name:{self.name}")

class Coffee(Drink):
    # def print_info(self):
    #     print(f"Coffee Self.name:{self.name}")
    pass

d= Drink("딸기 스무디")
c= Coffee("바나나 스무디")
print(c.name)

d.print_info()
c.print_info()
d.print_info()




