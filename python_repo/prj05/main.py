

age=int(input("나이?:"))
#
# if age<20:
#     print("미성년자")
#     if age<8:
#         print("미취학 아동")
#     elif age<14:
#         print("초등학생")
#     elif age<17:
#         print("중학생")
#     else:
#         print("고등학생")
# else:
#     print("성인")

group_age=(8,14,17,20)
group_clas=("미취학아동","초등학생","중학생","고등학생")

if age<20:
    dummy=False
    count=0
    print("미성년자 술과 담배를 팔지 마시오")
    while dummy==False:
        if age<group_age[count]:
            print(group_clas[count])
            dummy=True
        else:
            count=count+1
else:
    print("성인")


