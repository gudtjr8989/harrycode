#Introduction
print("Welcome to Tic Tac Toe")
print("Can you defeat me? If you do you get a 100$ as reward!")




##Innitiation========================================
#Computer Processing
hid_cor=[0,1,2,3] #hidden corner
hid_side=[0,1,2,3] #hidden side
hid_mid=0 #hidden mid
turn=0



#Display
display_corner=[0,1,2,3] #hidden corner
display_side=[0,1,2,3] #hidden side
display_mid=0 #hidden mid

#definning variables
cor_conv_fact=int(input("Cor_conv: "))
side_conv_fact=int(input("Side_conv: "))

#Defining Conversion Factor====================================================
# def input_cor_conv_fact():
#     cor_conv_fact=int(input("Cor_conv: "))
#     return cor_conv_fact
#
# def input_side_conv_fact():
#     side_conv_fact=int(input("Side_conv: "))
#     return side_conv_fact

# Converion =========
# input_cor_conv_fact()
print(f"Corner Convertion Factor:{cor_conv_fact}")
# input_side_conv_fact()
print(f"Side Convertion Factor:{side_conv_fact}")


#=Conversion Process===================
#Hid to Display function
# def hid_to_display_corner():
#     display_corner=[hid_cor[(cor_conv_fact+0)%4],hid_cor[(cor_conv_fact+1)%4],hid_cor[(cor_conv_fact+2)%4],hid_cor[(cor_conv_fact+3)%4]]
#     return display_corner
# hid_to_display_corner()
display_corner=[hid_cor[(cor_conv_fact+0)%4],hid_cor[(cor_conv_fact+1)%4],hid_cor[(cor_conv_fact+2)%4],hid_cor[(cor_conv_fact+3)%4]]
print(display_corner)

# def hid_to_display_side():
#     display_side=[hid_side[(side_conv_fact+0)%4],hid_side[(side_conv_fact+1)%4],hid_side[(side_conv_fact+2)%4],hid_side[(side_conv_fact+3)%4]]
#     return display_side
# hid_to_display_side()
display_side=[hid_side[(side_conv_fact+0)%4],hid_side[(side_conv_fact+1)%4],hid_side[(side_conv_fact+2)%4],hid_side[(side_conv_fact+3)%4]]
print(display_side)


disp_table_r3=[display_corner[3], display_side[2], display_corner[2]]
disp_table_r2=[display_side[1], hid_mid, display_side[3]]
disp_table_r1=[display_corner[0], display_side[0], display_corner[1]]

def display_board() : #표시 기능
    print("R3:",disp_table_r3)
    print("R2:",disp_table_r2)
    print("R1:",disp_table_r1)
    return

display_board()

