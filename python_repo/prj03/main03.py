#Practice
age=int(input("Enter your age:"))
x=0
if age<=0:
    print("Your age must be greater than 0")
else :
    if age < 30:
        x=x+1
        if age<10:
            print("Your are not a teenager yet")
        elif age<20:
            print("Your are a teenager yet")
        else:
            print("you are a an adult under 30")
    else:
        if age<40:
            print("you are in your 30s")
        elif age<50:
            print("you are a in your 40s")
        else:
            print("you are a over 50")

print(x)

