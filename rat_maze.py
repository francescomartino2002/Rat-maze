import pygame
import sys
import os
import time
import threading
from solver import solve_maze

pygame.init()

#solver
DIM = 10
start = [0,0]
end  = [DIM-1,DIM-1]
finish = False

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#window settings
WIDTH, HEIGHT = 600, 600
MARGIN = 3
BLOCK_SIZE = (WIDTH / 10) - MARGIN
clock = pygame.time.Clock()

pygame.display.set_caption('Rat Maze')
icon = pygame.image.load("rat.png")


pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = [[2,1,0,0,0,0,1,0,0,0],
        [0,1,0,1,0,1,1,1,0,0],
        [0,1,1,1,1,1,0,1,0,0],
        [0,0,1,0,0,1,0,0,1,0],
        [1,1,1,1,1,1,0,0,1,0],
        [0,1,0,0,1,0,0,1,1,0],
        [0,1,0,0,1,1,1,1,0,0],
        [0,1,1,0,0,1,0,0,0,0],
        [0,0,1,1,0,1,0,1,0,0],
        [0,0,0,0,0,1,1,1,1,1]]



def draw_Grid():
    for row in range(10):
        for column in range(10):
            color = black
            if grid[row][column] == 1:
                color = white
            elif grid[row][column] == 2:
                color = red
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + BLOCK_SIZE) * column + MARGIN,
                              (MARGIN + BLOCK_SIZE) * row + MARGIN,
                              BLOCK_SIZE,
                              BLOCK_SIZE])


t1 = threading.Thread(target = solve_maze, args=(0,0,0,0,grid))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    t1.start()

        screen.fill(black)
        draw_Grid()
            
            
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()

