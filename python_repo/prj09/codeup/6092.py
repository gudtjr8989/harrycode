#풀이 1
n=int(input())
attend=input("")
attend_list=attend.split()
count=[]

for x in range(0,23): # count=[0]*23
    count.append(0)

for x in range(0,len(attend_list)):
    attend_list[x]=int(attend_list[x])
    count[attend_list[x]-1]=count[attend_list[x]-1]+1

for x in range(0,len(count)):
    print(count[x],end=" ")

# #선생님 풀이
# n=input()
# x=input()
# list=x.split()
# memo=[0]*24
#
# for st_num in list:
#     st_num=int(st_num)
#     memo[st_num]=int(memo[st_num])+1
# for x in memo[1:24]:
#     print(x,end=" ")