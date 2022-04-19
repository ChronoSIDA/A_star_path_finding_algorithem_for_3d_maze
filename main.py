import numpy as np
import Algorithm
import MazeMaker
import matplotlib.pyplot as plt
import numpy as np

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import axes3d

def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

def plot_cube(val, position):
    n_cubes[position[0]][position[1]][position[2]] = True

def plot_now(n_cubes):
    facecolors = np.where(n_cubes, '#FFD65D4D', '#7A88CC03')
    # 26 15%
    # 4D 30%
    edgecolors = np.where(n_cubes, '#BFAB6E', '#7D84A61A')
    filled = np.ones(n_cubes.shape)

    # upscale the above voxel image, leaving gaps
    filled_2 = explode(filled)
    fcolors_2 = explode(facecolors)
    ecolors_2 = explode(edgecolors)

    # Shrink the gaps
    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
    x[0::2, :, :] += 0.05
    y[:, 0::2, :] += 0.05
    z[:, :, 0::2] += 0.05
    x[1::2, :, :] += 0.95
    y[:, 1::2, :] += 0.95
    z[:, :, 1::2] += 0.95

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)

    # # plt.show()
    # for angle in range(0, 360):
    #     plt.axis('off')
    #     ax.view_init(30, angle)
    #     plt.draw()
    #     plt.pause(.1)

    # print(n_cubes)




if __name__ == '__main__':
    # Demo
    # Pre-set example
    # make a 4 * 4 * 4 maze
    # maze = MazeMaker.ThreeDMaze()

    # A*
    val = input("Enter the size of maze you want to make: ")
    maze = MazeMaker.ThreeDMaze(int(val))
    n_cubes = np.zeros((int(val), int(val), int(val)), dtype=bool)
    voxels = np.zeros(int(val), int(val), dtype=bool)
    # print(maze.obstacle_positions)
    # print("Number of obstacles: " + str(len(maze.obstacle_positions)))
    for a in maze.obstacle_positions:
        # print(maze.obstacle_positions)
        # print("\nSize of obstacle " + str(maze.obstacle_positions.index(a) + 1) + ": " + str(int(np.sqrt(len(a)))) +
        #       " * " + str(int(np.sqrt(len(a)))))
        # print("Points in the obstacle: ")
        for b in a:
            plot_cube(val, b.get_position())

    plot_now(n_cubes)
    a_star = Algorithm.AStar(maze)
    path = a_star.run_algorithm()

    if len(path) != 0:
        re = "\n"
        for i in path:
            re += i.show_content()
            re += "\n"

        print(re)