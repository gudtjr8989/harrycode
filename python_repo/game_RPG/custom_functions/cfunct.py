def importcheck():
    print("cfunct successfully imported")

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
