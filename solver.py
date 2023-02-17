import os
import time

DIM = 10
start = [0,0]

# X -> rows
# Y -> columns
        
'''
def print_maze(matrix):
    #os.system('clear')
    for i in range(DIM):
        print(matrix[i])
    print('\n')
    time.sleep(0.5)
'''

finish = False

def solve_maze(new_x,new_y,x,y,grid):
    time.sleep(0.3)
    #past position
    last_x = x
    last_y = y
    #current position
    x = new_x
    y = new_y
    
    x_moves = [0, 1, 0, -1]
    y_moves = [1, 0, -1, 0]

    for i in range(4):
        global finish
        if finish == True:
            break
        new_x = x +  x_moves[i]
        new_y = y + y_moves[i]

        if new_x == DIM-1 and new_y == DIM-1:
            grid[new_x][new_y] = 2
            finish = True
            exit

        elif check_valid(new_x,new_y,grid) and (new_x != last_x or new_y != last_y):
            grid[new_x][new_y] = 2
            solve_maze(new_x,new_y,x,y,grid)
    
    if finish == False:
        grid[x][y] = 1
        time.sleep(0.3)
        
    return

#checks if next position is valid
def check_valid(x,y,grid):
    if x >= DIM or x < 0 or y >= DIM or y < 0:
        return 0
    elif grid[x][y] == 1:
        return 1
    else: return 0

