# from pokemon import Pokedex
#
# spd=[]
# for i in range(0,151):
#     spd.append(int(Pokedex[i][7]))
#
# min=150
# max=0
# for i in range(0,151):
#     if min > spd[i]:
#         min = spd[i]
#         print(i,"min:",min)
#     else:
#         pass
#     if max < spd[i]:
#         max = spd[i]
#         print(i,"max:",max)
#     else:
#         pass
# print(min,max)
#

table=[]
for x in range (50,201):
    a=round(10000 / (20 + x),1)
    b=round(10000 / (125 + x),1)
    c=round(a/b,2)
    d=round(b/a,2)
    table.append([x,c])

for i in range(0,len(table)):
    print(table[i])
