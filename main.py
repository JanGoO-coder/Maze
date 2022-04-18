from maze import Maze
from generator import recursive_backtrack

import pygame, time
pygame.init()

W = 600
H = 600
C = 50

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Maze")

maze = Maze(W, H, C)

def loop():
    isGenerated = False

    # set frame rate
    clock = pygame.time.Clock()
    FPS = 60
    clock.tick(FPS)

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isRunning = False
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