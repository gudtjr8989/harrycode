#dictionary

x= {
    "name":None,
    "attk":10,
    "hp":100
}
print(x)
print(type(x))
x["hp"]=200 # HP변경

print(x["name"])
print(x["attk"])
print(x["hp"])

y=x.get("nam") # 오타치더라도 오류 방지

print(y)
print("attk" in x)

#여러개 있는 데이터가 들어있는 덩어리를 불러와서 작업
for element in x.keys(): #각각 한줄
    print("=====")
    print(element)
    print(type(element))


# print(x.keys())
# print(x.values())
# print(x.items())
# print(type(x.keys),type(x.values),type(x.items))
