import pygame

def get_cord(dif, pos):
    global x
    x = int(pos[0]//dif)
    global y
    y = int(pos[1]//dif)
 
def highlight_box(screen, dif,x,y):
    for k in range(2):
        pygame.draw.line(screen, (0, 0, 0), (x * dif-3, (y + k)*dif), (x * dif + dif + 3, (y + k)*dif), 7)
        pygame.draw.line(screen, (0, 0, 0), ( (x + k)* dif, y * dif ), ((x + k) * dif, y * dif + dif), 7)

def colour_box(screen,dif,i,j,grid):
    pygame.draw.rect(screen, (165, 220, 175), (i * dif, j * dif, dif + 1, dif + 1))

# make the grid        
def draw(screen,font, dif,n, grid, colour_scheme=colour_box, values=[]):
    for i in range (n*n):
        for j in range (n*n):
            if grid[i][j]!= 0:
                colour_scheme(screen,dif,i,j,values)
                text1 = font.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))       
    for i in range(n*n+1):
        if i % n == 0 :
            thick = 5
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     

def fill_value(font, screen, dif,x,y, value):
    text = font.render(str(value), 1, (0, 0, 0))
    screen.blit(text, (x * dif + 15, y * dif + 15)) 

def raise_value_error(font, screen):
    text1 = font.render("wrong ! enter a valid key for the game", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 

def game_result(font, screen):
    text1 = font.render("game finished", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 

