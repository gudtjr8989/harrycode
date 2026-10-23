# def input_price():
#     while True:
#         x=input("도서 가격: ")
#         type_x=type(x)
#
#         if type_x == type("str"):
#             print("Error please type in the price in numerical numbers")
#         else:
#             x = int(x)
#             break
#             return x
#
# x=input_price()
# print(x)
#

def input_integer(message): #정수 검사 // 상태 완
    status=True
    test=True
    while status==True:
        x = input(message)
        for i in range(len(x)-1): #검사
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

