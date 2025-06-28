for row in range(7):
    for col in range(6):
        if ((row==0 or row==6 or row==3) and (col==2 or col==3 or col==4 or col==5)) or (col==1 and (row==1 or row==2 or row==3 or row==4 or row==5)) or (col==5 and(row==4 or row==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()