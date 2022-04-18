import pygame, sys

stack = []
visited = []

def recursive_backtrack(window, maze):

    maze.draw_maze(window)

    visited = [[False for i in range(maze.cols)] for j in range(maze.rows)]
    x, y = maze.current_row, maze.current_col
    visited[x][y] = True

    while any(visited):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        if len(maze.get_neighbors()) > 0:
            # choose random neighbor
            direction = maze.get_random_neighbor()

            if direction == 'up':
                x, y = maze.current_row, maze.current_col
                maze.carve_up()
                stack.append(maze.get_direction(x, y))
            if direction == 'down':
                x, y = maze.current_row, maze.current_col
                maze.carve_down()
                stack.append(maze.get_direction(x, y))
            if direction == 'left':
                x, y = maze.current_row, maze.current_col
                maze.carve_left()
                stack.append(maze.get_direction(x, y))
            if direction == 'right':
                x, y = maze.current_row, maze.current_col
                maze.carve_right()
                stack.append(maze.get_direction(x, y))

            visited[maze.current_row][maze.current_col] = True
        else:
            # backtrack
            if len(stack) > 0:
                direction = stack.pop()
            else:
                break

            if direction == 'up':
                maze.back_up()
            if direction == 'down':
                maze.back_down()
            if direction == 'left':
                maze.back_left()
            if direction == 'right':
                maze.back_right()

        pygame.time.delay(50)
        maze.draw_maze(window)
    return

    