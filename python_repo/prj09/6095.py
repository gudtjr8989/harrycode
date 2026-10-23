board=[]
for j in range(0,19): #y
    board.append([])
    for i in range(0,19): #x
        board[j].append(0)
# print(board)
# print(len(board))
# print(len(board[0]))
n=int(input())
x_coor=0
y_coor=0
for A in range(0,n):
    dummy = input()
    d = dummy.split()
    x_coor=int(d[0])-1
    y_coor=int(d[1])-1
    board[y_coor][x_coor]=1

for j in range(0,19):
    for i in range(0,19):
        print(board[i][j],end=' ')
    print()




