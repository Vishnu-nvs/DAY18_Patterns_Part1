for row in range(9):
    for col in range(7):
        if ((row==0 or row==8) and (col==2 or col==3 or col==4 or col==5)) or ((col==1 or col==6) and(row==1 or row==2 or row==3 or row==5 or row==6 or row==7)) or (row==4 and (col==2 or col==3 or col==4 or col==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()