# 상속 , super
class Drink():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print("나는 드링크야!")

    def __str__(self):
        return self.name, self.price

class Coffee(Drink):
    def __init__(self, shot,a,b):
        super().__init__(a,b)
        self.shot = shot

# class Latte(Coffee):
#     pass


latte=Drink("라떼",1500)
z=Coffee(2,latte.name, latte.price)
print(z.name,z.price,z.shot)
x=Coffee(2,"라떼",1500)
print(x.name)
print(x.price)
print(x.shot)
