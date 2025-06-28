# * * * * * 
# *
# * * * *   
#         * 
#         *
# * * * *



for row in range(6):
    for col in range(5):
        if row==0 or (col==0 and row<3) or ((row==2 or row==5 )and col<4) or (col==4 and (row==3 or row==4)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

