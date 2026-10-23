# #리스트
# x=["200","백만원",900,3.14,[2,3]]#요소들을=index는 0 부터
# print(x)
# print(type(x))
# print(type(x)=="list")
# print(x[4][1])
# x[4][1]=5
# x[3]="바보"
# print(x)
#
# #list 추가 증가 (맨뒤에 증가
# x.append("새로운요소")
# print(x)
# #list 지우기
# x.remove("바보")
# print(x)
# x.remove([2,5])
# x.append([0,0])
# x.append("새로운요소")
# print(x)
# print(len(x))
# print(len(x[4]))
#
# #리스트에 용하는 연산자 *list in은 완전 다르다
# print("바보" in x) #바보가 x에 있나?
# print("새로운요소" in x) #바보가 x에 있나?
# x.remove("새로운요소") # 오랜된 걸 먼저 지운다앞에
# print(x)

nums=[10,30,20,40,50,60,70,80,90,100]
nums.sort()
print(nums)
result=nums[1:4]#Slicing [x:y] x이상 y미만
print(nums[1:3])
#이미지는 2차원이다
#동영상은 3차원?



