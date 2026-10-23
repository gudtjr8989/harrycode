# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

letter=input("")
letter_case=("A","B","C","D")
letter_message=("best!!!","good!!","run!","slowly~")
dum=False
count=0
while dum==False:
    if count<4 and letter==letter_case[count]:
        print(f"{letter_message[count]}")
        dum=True
    elif count<4:
        count=count+1
    else:
        print("what?")
        dum=True