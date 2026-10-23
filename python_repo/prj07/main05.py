# import random
# for i in range(1,11):
#     print(i, end=" ")
#
# # x=0
# # for i in range (1,11):
# #     x=x+i
# # print(x)
# #
# # for i in range(1,11,2):
# #     print(i, end=" ")
#
#
# for i in range(1,20):
#     print(random.randint(1,20), end=" ")

# #복합연산자 +=, -=, 자기 자신에게 다음과 같이 연산
# x=0
# for i in range (1,11):
#     x+=i
# # print(x)
#
# #6077
# x=int(input())
# total=0
# for i in range(1,x+1):
#     if i%2==0:
#         total+=i
# print(total)
#6078#
# status=False
# while status==False:
#     x=input("")
#     print(x)
#     if x=="q":
#         break
# # #6079
# top=int(input())
# total=0
# for x in range(1,top+1):
#     total+=x
#     if total>=top:
#         print(x)
#         break

n=int(input())
m=int(input())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)
