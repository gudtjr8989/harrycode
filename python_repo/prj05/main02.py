#숫자

num=int(input(""))

if num>0:
    if num%2==0:
        print("C")
    else:
        print("D")
elif num<0:
    if num%2==0:
        print("A")
    else:
        print("B")
else:
    pass
