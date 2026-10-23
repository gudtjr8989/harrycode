# 도서관리
# title: price

book_list=[]

while True:
    t=input("Title?:")
    p=int(input("Price?:"))
    x={"title":t,
        "price":p}
    book_list.append(x)
    q=input("Do u want to continue?")
    if q=="n":
        break
print(book_list)
for d in book_list:
    print(f"{d["title"]} {d["price"] }")
print(book_list)