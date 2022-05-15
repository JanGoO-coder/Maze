from maze import Maze
from generator import recursive_backtrack
from pathfinder import find_path

import pygame, time
pygame.init()

W = 1000
H = 800
C = 20

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Maze")

# change icon of window
icon = pygame.image.load("./assets/maze-icon.svg")
pygame.display.set_icon(icon)

maze = Maze(W, H, C)

def loop():
    isGenerated = False

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isRunning = False
                if event.key == pygame.K_g:
                    maze.to_graph()
                if event.key == pygame.K_f:
                    find_path(window, maze)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isRunning = True
                    if not isGenerated:
                        maze.show_start_and_end()
                        maze.draw_maze(window)
                        pygame.time.delay(500)
                        maze.hide_start_and_end()
                        recursive_backtrack(window, maze)
                        isGenerated = True
                        maze.show_start_and_end()
                        pygame.time.delay(2000)
                if event.button == 3:
                    isGenerated = False
                    maze.reset()

            maze.draw_maze(window)

def main():
    loop()
    pygame.quit()
    
if __name__ == "__main__":
    main()