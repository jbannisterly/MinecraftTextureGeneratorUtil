import numpy as np

def fillGrid(size: int):
    offset = 0.5
    grid = np.zeros((size + 1, size + 1, size + 1))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                distance = (i + offset) ** 2 + (j + offset) ** 2 + (k + offset) ** 2
                if distance < size ** 2:
                    grid[i, j, k] = 1
    return grid

def createCubes(grid, size: int):
    cubeList = []
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if grid[i, j, k] == 1 and grid[i + 1, j, k] == 0 and grid[i, j + 1, k] == 0 and grid[i, j, k + 1] == 0:
                    cubeList.append((i + 1, j + 1, k + 1))
    return cubeList