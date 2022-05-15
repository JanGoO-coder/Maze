import networkx as nx
import matplotlib.pyplot as plt
import pygame

def find_path(window, maze):
    G = maze.to_graph()
    path = nx.shortest_path(G, maze.start_node, maze.end_node)

    new_g = nx.Graph()
    new_g.add_nodes_from(path)
    for i in range(len(path) - 1):
        new_g.add_edge(path[i], path[i+1])
    nx.draw(new_g, with_labels=True)
    # plt.show()

    rows = []
    cols = []

    for p in path:
        for i in range(maze.rows):
            for j in range(maze.cols):
                if maze.nodes_data[i * maze.cols + j]['id'] == p:
                    rows.append(i)
                    cols.append(j)

    cords = []
    for i in range(len(rows)):
        cords.append((rows[i], cols[i]))

    for cord in cords:
        maze.maze[cord[0]][cord[1]][0] = 'G'
        maze.draw_maze(window)
        # pygame.time.delay(50)


    maze.show_start_and_end()

