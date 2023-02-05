import pygame 
import validate
import backtracking
import simulated_annealing
import display
import numpy as np

n = 3

pygame.font.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku")
 
x = 0
y = 0
dif = 500 / (n*n)
val = 0
grid = np.zeros((n*n,n*n), dtype = np.int8)
font = pygame.font.SysFont('ariel',40)

move = False
solve = False
annealing = False
finished = False
error = 0
value = -1

run = True

while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            move = True
            pos = pygame.mouse.get_pos()
            display.get_cord(dif, pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                move = True
            if event.key == pygame.K_RIGHT:
                x+= 1
                move = True
            if event.key == pygame.K_UP:
                y-= 1
                move = True
            if event.key == pygame.K_DOWN:
                y+= 1
                move = True  
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2   
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9 
            if event.key == pygame.K_s:
                solve = True
            if event.key == pygame.K_a:
                annealing = True
            if event.key == pygame.K_d:
                grid = np.array(   [[5,3,0,0,7,0,0,0,0],
                                    [6,0,0,1,9,5,0,0,0],
                                    [0,9,8,0,0,0,0,6,0],
                                    [8,0,0,0,6,0,0,0,3],
                                    [4,0,0,8,0,3,0,0,1],
                                    [7,0,0,0,2,0,0,0,6],
                                    [0,6,0,0,0,0,2,8,0],
                                    [0,0,0,4,1,9,0,0,5],
                                    [0,0,0,0,8,0,0,7,9]])
            if event.key == pygame.K_BACKSPACE:
                value = 0
            if event.key == pygame.K_r:
                grid = np.zeros((n*n,n*n), dtype = np.int8)
    if solve:
        result = backtracking.backtrack(screen,font,dif,grid,n)
        if type(result) is not np.ndarray:
            error = 1
        else:
            grid = result
            finished = True
        solve = False   
    if annealing:
        result = simulated_annealing.simulated_annealing(screen,font,dif,grid,n=n)
        grid = result
        finished=True
        annealing=False
    if value != -1:           
        if value == 0:
            grid[x][y]= value
        else:
            display.fill_value(font,screen,dif,x,y,value)
            if validate.valid(grid , x, y, value):
                grid[x][y]= value
                move = False
            else:
                grid[x][y]= 0
                display.raise_value_error(font,screen)  
        value = -1   
       
    if finished:
        display.game_result(font,screen)       
    display.draw(screen,font,dif,n,grid) 
    if move:
        display.highlight_box(screen,dif,x,y)      
 
    pygame.display.update() 
pygame.quit()    
    