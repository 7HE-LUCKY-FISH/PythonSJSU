def printspace(space):
    if (space == 0):
        return
    print(" ", end="")
    printspace(space -1)

def printstar(star):
    if (star == 0):
        return
    print("* ", end="")
    printstar(star-1)
    
def printdiamond(n, current_row):
    if(current_row> n):
        return
    printspace(n- current_row)
    printstar(current_row)
    print()
    '''
    if(current_row == n):
        printdiamond(n-1,current_row+1)
    else:
        printdiamond(n, current_row+1)
    '''
    printdiamond(n,current_row+1)
  
    if(current_row<n):
        printspace(n-current_row)
        printstar(current_row)
        print()

if __name__ == "__main__":
    n = float(input("Enter number of rows: "))
    printdiamond(n, 1)
