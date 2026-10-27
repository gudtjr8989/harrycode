class coffee:
    shop = "파이썬 까페"
    def __init__(self, name):
        self.name = name



a = coffee("아메리카노")
b = coffee("라때")

print(a.shop)
print(b.shop)

a.shop="돈크워 까페" #instance 변수
coffee.shop="다크워 까페"
print(a.shop)
print(b.shop)
a.shop=coffee.shop
coffee.shop="파워 까페"
print(a.shop)
print(b.shop)

