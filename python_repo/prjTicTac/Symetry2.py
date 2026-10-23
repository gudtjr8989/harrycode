board=[[0,1,2],[3,4,5],[6,7,8]]
temp_board=[[0,0,0],[0,0,0],[0,0,0]]
print(board[2])
print(board[1])
print(board[0])
x=0
y=0
cal_x=0
cal_y=0
def input_calculations():
    cal_x=x-2
    cal_y=y-2
    return cal_x,cal_y
input_calculations()

print(cal_x,cal_y)
