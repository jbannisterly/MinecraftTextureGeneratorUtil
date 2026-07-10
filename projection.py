import cv2
import numpy as np
from atlas import Atlas

example = cv2.imread("res/example.png")

# create the cubes for a sphere
cubes = [
    [16, 6, 6],
    [14, 10, 10],
    [6, 6, 16],
    [10, 10, 14],
    [12, 12, 12],
    [10, 14, 10],
    [6, 16, 6]
]
atlas = Atlas((128, 128, 3))
for cube in cubes:
    atlas.addCube(example, cube, [16 - cube[0], 16 - cube[1]])

cv2.imwrite("res/example_copy.png", atlas.atlas)

print("Texture offsets")
print(atlas.offsets)