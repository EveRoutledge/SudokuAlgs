import random
import math
import numpy as np
import display
import pygame
import copy

def colour_box_badness(screen,dif,i,j,values):
    val = values[i][j]
    if val == -1:
        pygame.draw.rect(screen, (165, 220, 175), (i * dif, j * dif, dif + 1, dif + 1))
    elif val== 0:
        pygame.draw.rect(screen, (0, 255, 0), (i * dif, j * dif, dif + 1, dif + 1))
    elif val<3:
        pygame.draw.rect(screen, (255, 255, 0), (i * dif, j * dif, dif + 1, dif + 1))
    elif val<5:
        pygame.draw.rect(screen, (255, 166, 0), (i * dif, j * dif, dif + 1, dif + 1))
    elif val<7:
        pygame.draw.rect(screen, (255, 68, 0), (i * dif, j * dif, dif + 1, dif + 1))   
    else:
        pygame.draw.rect(screen, (255, 0, 0), (i * dif, j * dif, dif + 1, dif + 1))


def simulated_annealing(screen,font,dif,grid,schedule=None,max_t=2000,tau = 100,epsilon = 0.00001, n=3):
    if schedule == None:
        iterable = (math.exp(-i/tau) for i in range(max_t))
        schedule = np.fromiter(iterable,float)
    badness_grid = init_badness_grid(grid)
    current = fill_init_grid(grid)
    badness_val, badness_grid = update_badness_grid(current,badness_grid,n)
    # add best
    t=0
    while t < max_t:
        T = schedule[t]
        if T <= epsilon:
            continue
            #return current
        else:
            succ = gen_successor_v2(current,badness_grid,n)
            new_badness_val, new_badness_grid = update_badness_grid(succ, badness_grid,n)
            if new_badness_val == 0:
                return succ
            delta_e = badness_val - new_badness_val
            if delta_e >= 0:
                current = succ
                badness_val = new_badness_val
                badness_grid = new_badness_grid
            else:
                if random.random() < math.exp(delta_e/T):
                    current = succ
                    badness_val = new_badness_val
                    badness_grid = new_badness_grid
        if t%1==0:
            screen.fill((255, 255, 255))
            display.draw(screen,font,dif,n,current,colour_box_badness,badness_grid)
            pygame.display.update()
            pygame.time.delay(20)
        t=t+1
    return current

def init_badness_grid(grid):
    temp = np.empty((len(grid),len(grid)))
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]!=0:
                temp[i][j] = -1
    return temp

def update_badness_grid(grid,badness_grid,n):
    temp = np.empty((len(grid),len(grid)))
    for i in range(len(grid)):
        for j in range(len(grid)):
            if badness_grid[i][j]==-1:
                temp[i][j] = -1
            else:
                temp[i][j] = cell_badness(grid,i,j,n)
    sum = np.sum(temp) + np.count_nonzero(temp==-1)
    return sum, temp
    #badness = np.fromfunction(lambda i,j: 0 if badness_grid[i][j] == -1 else cell_badness(grid,i,j,n),(len(grid),len(grid)))
    #return np.sum(badness), badness

def fill_init_grid(grid):
    temp = np.empty((len(grid),len(grid)),int)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]!=0:
                temp[i][j] = grid[i][j]
            else:
                temp[i][j] = random.randint(1,9)
    return temp
    #return np.fromfunction(lambda i,j: grid[i][j] if grid[i][j]!=0 else random.randint(1,9),(len(grid),len(grid)), dtype=int)

def gen_successor(grid, badness_grid, n):
    counter = 0
    temp = copy.copy(grid)
    while counter<10:
        coords = np.unravel_index(np.argmax(badness_grid), badness_grid.shape)
        bad = badness_grid[coords[0]][coords[1]]
        val = grid[coords[0]][coords[1]]
        for i in range(1,n*n+1):
            if i != val:
                temp[coords[0]][coords[1]] = i
                if cell_badness(temp, coords[0], coords[1], n)<bad:
                    return temp
        badness_grid[coords[0],coords[1]] = 0
        counter+=1
    while True:
        x = random.randint(0,8)
        y = random.randint(0,8)
        if badness_grid[x][y]!=-1:
            grid[x][y] = random.randint(1,9)
            return grid


def cell_badness(grid,x,y,n):
    value = grid[x][y]
    bad = 0
    for i in range(n*n):
        if grid[x][i] == value:
            if i != y:
                bad+=1
        if grid[i][y] == value:
            if i != x:
                bad+=1
    large_row = (x//n) * n
    large_col = (y//n) * n
    for i in range(large_row, large_row + n):
        for j in range (large_col, large_col + n):
            if grid[i][j] == value:
                if not (i == x and j == y):
                    bad += 1
    return bad


def gen_successor_v2(grid, badness_grid, n):
    counter = 0
    temp = copy.copy(grid)
    row = np.random.randint(0,9)
    permutation = np.random.permutation(np.arange(1,n*n+1))
    for i in range(n*n):
        if badness_grid[row][i] == -1:
            permutation = np.delete(permutation,np.where(permutation==grid[row][i])[0])
    for i in range(n*n):
        if badness_grid[row][i]!=-1:
            temp[row][i] = permutation[0]
            permutation = permutation[1:]
    return temp