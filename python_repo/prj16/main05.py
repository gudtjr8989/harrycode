class Coffee:
    def __init__(self, name, price):
        print(f'{name}init Coffee 호출됨')
        self.name = name
        self.price = price

    def __str__(self):
        print("__str__ 호출됨")
        return f"{self.name}/ {self.price}"

    def __eq__(self, other):
        print("eq 호출됨")
        return

    

x = Coffee('americano', 1000)
print(x==1)
print(x.name)
