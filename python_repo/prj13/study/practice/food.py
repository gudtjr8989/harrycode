class Food:
    def __init__(self,name,type,place,price,style,descr,calories):
        self.name = name
        self.type = type
        self.place = place
        self.price = price
        self.style = style
        self.descr = descr
        self.calories = calories


    def __str__(self):
        return f"{self.name} {self.type} {self.place} {self.price} {self.style} {self.descr}/{self.calories}"