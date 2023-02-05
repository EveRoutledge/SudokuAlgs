import copy
import display
import validate
import pygame
import numpy as np

def backtrack(screen,font,dif,board, n=3):
    new_board = copy.deepcopy(board)
    pygame.event.pump()
    for i in range(n*n):
        for j in range(n*n):
            if board[j][i] == 0:
                for k in range(1,n*n+1):
                    if validate.valid(board, j,i, k):
                        new_board[j][i] = k

                        screen.fill((255, 255, 255))
                        display.draw(screen,font,dif,n,new_board)
                        display.highlight_box(screen,dif,j,i)
                        pygame.display.update()
                        pygame.time.delay(20)

                        result = backtrack(screen,font,dif,new_board,n)
                        if type(result) is np.ndarray:
                            return result
                screen.fill((255, 255, 255))
                display.draw(screen,font,dif,n,board)
                display.highlight_box(screen,dif,j,i)
                pygame.display.update()
                pygame.time.delay(50)
                return False
    return board
    
    