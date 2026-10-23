#y=1축 회전 (양옆 반전)
    # y값에 *-1곱

conv_y=1
conv_y_factor=False#변환 해야하는가?
set_conv_y_factor=False# 변환 조건을 충족했는가?
if conv_y_factor==False :#(y축 회전 on-off)
    conv_y*=-1*conv_y
#x=1축 회전(위아래 반전)
    # x값에*-1곱
conv_x=1
conv_x_factor=False #변환 해야하는가?
set_conv_x_factor=False # 변환 조건을 충족했는가?
if conv_x_factor==True
    conv_x*-1

# x=1 축회전
    # x y 변경
conv_x_1_factor=False
set_conv_x_1_factor=False
if conv_x_1_factor==True
    conv_x=conv_x_1_factor+not conv_x_1_factor*conv_y


#y=1축 회전 (양옆 반전)
    # y값에 *-1곱
conv_y=1 #
conv_y_factor=0#변환 해야하는가?
set_conv_y_factor=False# 변환 조건을 충족했는가?
if conv_y_factor==1:#(y축 회전 on-off)
    conv_y*=-1*conv_y

#x=1축 회전(위아래 반전)
    # x값에*-1곱
conv_x=1
conv_x_factor=0 #변환 해야하는가?
set_conv_x_factor=False # 변환 조건을 충족했는가?
if conv_x_factor==1:
    conv_x*-1

# x=1 축회전
    # x y 변경
conv_x_1_factor=0
set_conv_x_1_factor=False
if conv_x_1_factor==1




for i in range(1,3+1):
    for j in range(1,3+1):
        temp_board[(i-1)][(j-1)]=board[(i-1)][(j-1)]




#y=1축-회전
    # x-2값에 *-1곱


# #Paired Conversion Factor
# conv_x_factor=False
# set_x_factor=False
#
# conv_y_factor=True
# set_y_factor=False
#
# conv_x_1_factor=False
# set_x_1_factor=False
#
# conv_x_neg_1_factor=False
# set_x_neg_1_factor=False
#

print(temp_board[2])
print(temp_board[1])
print(temp_board[0])



# x=1 축회전
    # x y 변경
# x-=-1 축회전
    # -1 곱 후 자리변경

