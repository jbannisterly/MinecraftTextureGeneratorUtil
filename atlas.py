import cv2
import numpy as np
from cube import Cube

class Atlas:
    def __init__(self, atlas_size):
        self.atlas = np.zeros(atlas_size)
        self.offset = [0, 0]

    def addCube(self, source_image, size, offset):
        cube = Cube()
        cube.stretch(source_image, size, offset)
        cube.writeimage(self.atlas, self.offset)
        self.offset[1] += cube.z + cube.y

example = cv2.imread("res/example.png")

# example values
atlas = Atlas((64, 64, 3))
atlas.addCube(example, [4, 8, 8], [0, 0])
atlas.addCube(example, [8, 2, 4], [4, 4])

cv2.imwrite("res/example_copy.png", atlas.atlas)