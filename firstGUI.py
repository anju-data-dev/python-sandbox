picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]]

for row in picture:
    for index in row:
        if index==0:
            print(" ",end='')
        else:
            print("*", end='')

    print('')
  
    