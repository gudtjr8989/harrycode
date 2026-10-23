display_board=[]
for y in range(0,19):
    display_board.append([])
    for x in range(0,19):
        display_board[y].append(0)


def print_board(): # Return은 한개 값만 반환 할수 있다
    for y in range(len(display_board)-1,0,-1):
        print(f"R{y+1} |",end="")

        for x in range(len(display_board[y])):
            print(display_board[y][x],end="")
        print()
# display_board[18][12]=1
print_board()
