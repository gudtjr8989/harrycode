#1 int(input(")) with 내부 검사
def input_int(message): #정수 검사 // 상태 완
    status=True
    test=True
    while status==True:
        x = input(message)
        for i in range(0,len(x)): #검사
            if x[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
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

def input_only(message,e_message,crit): #정수 검사 // 상태 완
    status=True
    test=True
    while status==True:
        x = input(message)
        for i in range(0,len(x)): #검사
            if x[i] in crit:
                pass
            else:
                test = False
                break
        if test==False:
            print(e_message)
            continue
        else:
            break
    return x

#Test
x=input_only("in put a choice between A B C:","please choose between A B C",["A","B","C"])
# x=input_int("Int:")

print(x)
# print(x)

