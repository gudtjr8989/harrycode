#tupple=() 아니면 그냥 comma (여러개를 comma가 핵심) list 랑 비슷 수정이 불가
x=10,20,30
print(x)
print(type(x))
x=(10,20,30)
print(x)
print(type(x))

#set={} *순서가 없는대신 중복을 자동 제거
x={10,20,30,38,50,20}
print(x)
print(type(x))
#dict={key:value}
x={
    "id":"user01",
    "pwd":"1234",
    "nick":"death",
    "nick":"guest",
    "alias":"1dragon"
}
print(x) #Key에 대하서는 중복일시 덮어씨움
x["nick"]="joker"
print(x)
#자료구조

