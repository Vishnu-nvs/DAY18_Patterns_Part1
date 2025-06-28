print("\n")
for row in range (10):
    for col in range(13):
        if row==3 or row==9 or (row==0 and col>3) or row+col==3 or (row==5 and col==3) or (col-row==3 and row<4) or ((col==6 or col==0) and row>2) or  (col==12 and row>0) or ((col==2 or col==4)and row>4):
            print("*",end="     ")
        else:
            print(" ",end="     ")
            
    print()
    print()
    
    