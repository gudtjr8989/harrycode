list=[[1,2,3],[4,5,6],[7,8,9]]

rotate_x_axis=True



def rotate_x1_axis(y):
    if rotate_x_axis==True:
        temp_y=(y-1-1)*-1+1
        y=temp_y
        return y

def simulate():
    print(list[0])
    print(list[1])
    print(list[2])
    coord=input("Please type in the x y coordinates: ex) 2 4: ")
    coord=coord.split(" ")
    for x in range(0,len(coord)):
        coord[x]=int(coord[x])
    return coord
coord=simulate()
print(coord)
simulate()









