import pygame, random
import networkx as nx
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, w, h, c):
        self.rows = (h - 100) // c
        self.cols = (w - 100) // c
        self.cell_size = c
        self.edges = []
        self.graph = None

        # self.maze[row][col][0] == 'W' is for white rectangle
        # self.maze[row][col][0] == 'G' is for grey rectangle
        # self.maze[row][col][0] == 'B' is for Black rectangle
        # self.maze[row][col][0] == 'S' is for red rectangle
        # self.maze[row][col][0] == 'E' is for green rectangle
        # self.maze[row][col][0] == 'C' is for blue rectangle
        # self.maze[row][col][1] == '1' is for top wall and '0' is for no wall
        # self.maze[row][col][2] == '1' is for bottom wall and '0' is for no wall
        # self.maze[row][col][3] == '1' is for left wall and '0' is for no wall
        # self.maze[row][col][4] == '1' is for right wall and '0' is for no wall
        self.maze = [[['G', '1', '1', '1', '1'] for x in range(self.cols)] for y in range(self.rows)]
        
        self.start_row = 0
        self.start_col = 0
        self.end_row = self.rows - 1
        self.end_col = self.cols - 1
        self.current_row = self.start_row
        self.current_col = self.start_col

        self.maze[self.current_row][self.current_col][0] = 'S'
        self.maze[self.end_row][self.end_col][0] = 'E'

    def reset(self):
        self.__init__(self.cell_size * self.cols + 100, self.cell_size * self.rows + 100, self.cell_size)

    def get_neighbors(self):
        neighbors = []
        if self.current_row > 0 and self.maze[self.current_row - 1][self.current_col][0] != 'W':
            neighbors.append('up')
        if self.current_row < self.rows - 1 and self.maze[self.current_row + 1][self.current_col][0] != 'W':
            neighbors.append('down')
        if self.current_col > 0 and self.maze[self.current_row][self.current_col - 1][0] != 'W':
            neighbors.append('left')
        if self.current_col < self.cols - 1 and self.maze[self.current_row][self.current_col + 1][0] != 'W':
            neighbors.append('right')
        return neighbors

    def get_random_neighbor(self):
        neighbors = self.get_neighbors()
        if len(neighbors) > 0:
            return neighbors[random.randint(0, len(neighbors) - 1)]
        else:
            return None

    def remove_wall(self, row, col, direction):
        if direction == 'up':
            self.maze[row][col][1] = '0'
            self.maze[row - 1][col][2] = '0'
            index = row * self.cols + col
            next_index = (row - 1) * self.cols + col
            self.edges.append((index, next_index))
        if direction == 'down':
            self.maze[row][col][2] = '0'
            self.maze[row + 1][col][1] = '0'
            index = row * self.cols + col
            next_index = (row + 1) * self.cols + col
            self.edges.append((index, next_index))
        if direction == 'left':
            self.maze[row][col][3] = '0'
            self.maze[row][col - 1][4] = '0'
            index = row * self.cols + col
            next_index = row * self.cols + col - 1
            self.edges.append((index, next_index))
        if direction == 'right':
            self.maze[row][col][4] = '0'
            self.maze[row][col + 1][3] = '0'
            index = row * self.cols + col
            next_index = row * self.cols + col + 1
            self.edges.append((index, next_index))

    def move_up(self):
        if self.current_row > 0 and self.maze[self.current_row - 1][self.current_col][0] != 'W':
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_row -= 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def back_up(self):
        if self.current_row > 0:
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_row -= 1
            self.maze[self.current_row][self.current_col][0] = 'C'
    
    def move_down(self):
        if self.current_row < self.rows - 1 and self.maze[self.current_row + 1][self.current_col][0] != 'W':
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_row += 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def back_down(self):
        if self.current_row < self.rows - 1:
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_row += 1
            self.maze[self.current_row][self.current_col][0] = 'C'
    
    def move_left(self):
        if self.current_col > 0 and self.maze[self.current_row][self.current_col - 1][0] != 'W':
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_col -= 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def back_left(self):
        if self.current_col > 0:
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_col -= 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def move_right(self):
        if self.current_col < self.cols - 1 and self.maze[self.current_row][self.current_col + 1][0] != 'W':
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_col += 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def back_right(self):
        if self.current_col < self.cols - 1:
            self.maze[self.current_row][self.current_col][0] = 'W'
            self.current_col += 1
            self.maze[self.current_row][self.current_col][0] = 'C'

    def get_direction(self, row, col):
        if row < self.current_row:
            return "up"
        if row > self.current_row:
            return "down"
        if col < self.current_col:
            return "left"
        if col > self.current_col:
            return "right"

    def carve_up(self):
        self.remove_wall(self.current_row, self.current_col, 'up')
        self.move_up()
    
    def carve_down(self):
        self.remove_wall(self.current_row, self.current_col, 'down')
        self.move_down()

    def carve_left(self):
        self.remove_wall(self.current_row, self.current_col, 'left')
        self.move_left()

    def carve_right(self):
        self.remove_wall(self.current_row, self.current_col, 'right')
        self.move_right()

    def show_start_and_end(self):
        self.maze[self.start_row][self.start_col][0] = 'S'
        self.maze[self.end_row][self.end_col][0] = 'E'

    def hide_start_and_end(self):
        self.maze[self.start_row][self.start_col][0] = 'G'
        self.maze[self.end_row][self.end_col][0] = 'G'

    def draw_maze(self, window):
        window.fill((255, 255, 255))

        offset = 50
        padding = 6
        color = (255, 255, 255)
        ww = 1 # wall width

        # draw rectangle around maze
        pygame.draw.rect(window, (0, 0, 0), (offset - padding, offset - padding, self.cols * self.cell_size + padding * 2, self.rows * self.cell_size + padding * 2), padding)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col][0] == 'W':
                    color = (255, 255, 255)
                if self.maze[row][col][0] == 'G':
                    color = (220, 220, 220)
                if self.maze[row][col][0] == 'B':
                    color = (0, 0, 0)
                if self.maze[row][col][0] == 'S':
                    color = (255, 0, 0)
                if self.maze[row][col][0] == 'E':
                    color = (0, 255, 0)
                if self.maze[row][col][0] == 'C':
                    color = (0, 0, 255)

                pygame.draw.rect(window, color, (col * self.cell_size + padding + offset, row * self.cell_size + padding + offset, self.cell_size - padding * 2, self.cell_size - padding * 2))
                
                if self.maze[row][col][1] == '1': # top wall
                    pygame.draw.line(window, (0, 0, 0), (col * self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                if self.maze[row][col][2] == '1': # bottom wall
                    pygame.draw.line(window, (0, 0, 0), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                if self.maze[row][col][3] == '1': # left wall
                    pygame.draw.line(window, (0, 0, 0), (col * self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                if self.maze[row][col][4] == '1': # right wall
                    pygame.draw.line(window, (0, 0, 0), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
               
                # if self.maze[row][col][1] == '0': # top wall
                #     pygame.draw.line(window, (255, 255, 255), (col * self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                if self.maze[row][col][2] == '0': # bottom wall
                    pygame.draw.line(window, (255, 255, 255), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                if self.maze[row][col][3] == '0': # left wall
                    pygame.draw.line(window, (255, 255, 255), (col * self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                # if self.maze[row][col][4] == '0': # right wall
                #     pygame.draw.line(window, (255, 255, 255), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + offset), (col * self.cell_size + self.cell_size + offset, row * self.cell_size + self.cell_size + offset), ww)
                
        pygame.display.update()

    def to_graph(self):
        g = nx.Graph()
        no_of_cells = self.rows * self.cols

        g.add_nodes_from([i for i in range(no_of_cells)])

        colors = ["grey" for i in range(no_of_cells)]
        colors[self.start_row * self.cols + self.start_col] = "red"
        colors[self.end_row * self.cols + self.end_col] = "green"

        self.start_node = self.start_row * self.cols + self.start_col
        self.end_node = self.end_row * self.cols + self.end_col

        self.nodes_data = []

        for row in range(self.rows):
            for col in range(self.cols):
                self.nodes_data.append({
                    "id": row * self.cols + col,
                    "x": col,
                    "y": row,
                })

        g.add_edges_from(self.edges)

        self.graph = g
        nx.draw(g, with_labels=True, node_color=colors)
        plt.show()

        return g

    def print_maze_data(self):
        for row in self.maze:
            for cell in row:
                print(f"{cell[0]}{cell[1]}{cell[2]}{cell[3]}{cell[4]}", end=" ")
            print()