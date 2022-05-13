def check_valid_move(grid,row,column,num):     

    for i in range(0,9):
        if grid[row][i]==num:
            return False

    for x in range(0,9):
        if grid[x][column]==num:
            return False        
    th1 = row - row % 3                         
    th2 = column - column % 3 

    for i in range (0,3):
        for x in range(0,3):
            if grid[th1+i][th2+x]==num:
                return False
    return True

def solve(grid,row,column):

    if(column == 9):
        if(row == 8):
            return True
        column = 0
        row +=1
    if grid[row][column]>0:
        solve(grid,row,column+1)
    for num in range(1,10):
        if check_valid_move(grid,row,column,num):
            grid[row][column]=num
            
        

