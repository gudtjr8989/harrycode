n=input()
x=input()
list=x.split()

y=int(list[0])
for i in range(1,len(list)):
    if y>int(list[i]):
        y=int(list[i])
print(y)
