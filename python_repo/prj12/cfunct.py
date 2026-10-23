#1. int(input(")) with 내부 검사
def input_int(message): #정수 검사 // 상태 완료
    test=True
    while True:
        x = input(message)
        for i in range(0,len(x)): #검사
            if x[i] in "1234567890":
                test=True
                pass
            else:
                test = False
                break
        if test==False:
            print("Error! Please retry")
            continue
        else:
            x=int(x)
            break
    return x
    #Test
# x=input_int("Int:")
# print(x)



# 2. 특정 값만 input
def input_only(message,e_message,crit): #정수 검사 // 상태 완
    status=True
    test=True
    while status==True:
        x = input(message)
        for i in range(0,len(x)): #검사
            if x[i] in crit:
                test=True
                pass
            else:
                test = False
                break
        if test==False:
            print(e_message)
            continue
        else:
            return x
    #Test
# x=input_only("Please type in Y/y,N,n","Error!","YyNn")
# print(x)


def gcd(a,b):
    r=1
    if b>=a:
        y=b
        x=a
    if a>b:
        y=a
        x=b
    while r!=0:
        r=y%x
        print(x,y,r)
        y=x
        x=r
    print(f"the greatest common divisor of {a} and {b} is {x}")
    return x


# #Test
# x=input_only("in put a choice between A B C:","please choose between A B C",["A","B","C"])

#

# # print(x)

# x=input_only("","","1234567890")
# print(x)
#
# gcd(2,13)
