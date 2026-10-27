from main import item_database
#공항
class Items():
    def __init__(self, name, price=0,cost=0,qty=0): #4개변수
        self.name = name
        self.price = price
        self.cost = cost
        self.qty = qty
        self.revenue= price*qty
        self.profit = self.revenue-cost
    def display_customer_info(self):
        print(self.name)
        print(self.price)
    def display_manager_info(self):
        print(self.name)
        print(self.price)
        print(self.qty)
    def __str__(self):
        return self.name,self.price,self.cost,self.qty


#8개 2 세부 항목
class Drink(Items):
    def __init__(self, name, price, cost, qty,shop,volume,alcohol,vendor):
        super().__init__(a, b, c, d)
        self.shop = shop
        self.volume = volume
        self.alcohol = alcohol
        self.vendor = vendor
    def __str__(self):
        return self.name,self.price,self.cost,self.qty,self.volume,self.alcohol,self.vendor
    def list_append(self):
        item_database.append([self.name,self.price,self.cost,self.qty,self.volume,self.alcohol,self.vendor])











    pass
class Food(Items):
    pass
class Utility(Items):
    pass
class Service(Items):
    pass
class Gifts(Items):
    pass
class Books(Items):
    pass
class Movie(Items):
    pass
class Hotel(Items):
    pass




