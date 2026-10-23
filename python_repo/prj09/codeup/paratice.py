#이상한 숫자 부르기
x= "hello world"
print(x.split())
x ="1 3 5 7 9 10"
print(x.split())
num_list=x.split()
print("===========")
print(num_list)
print(type(num_list))
print(len(num_list))
print(type(len(num_list)))
for x in range(0,len(num_list)):#+1
    print(num_list[x])
