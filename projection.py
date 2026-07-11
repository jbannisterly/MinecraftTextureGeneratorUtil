import cv2
import numpy as np
from atlas import Atlas
import sphere_generator
import code_gen

example = cv2.imread("res/example.png")

# create the cubes for a sphere
gen_cubes = sphere_generator.createCubes(sphere_generator.fillGrid(8), 8)
cubes = [[i * 2, j * 2, k * 2] for (i, j, k) in gen_cubes]
atlas = Atlas((256, 256, 3))
for cube in cubes:
    atlas.addCube(example, cube, [16 - cube[0], 16 - cube[1]])

cv2.imwrite("res/example_copy.png", atlas.atlas)

code_gen.genCode(atlas.offsets, cubes)