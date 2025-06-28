#         **  
# *     * **  
#   * *   **  
#   * *   **  
# *     * **  
#         **  
for row in range(6):
    for col in range(5):
        if col==4 :
            print("**",end="  ")
        elif col+row==4 or row-col==1:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
