import cv2
import numpy as np
from cube import Cube

class Atlas:
    def __init__(self, atlas_size):
        self.atlas = np.zeros(atlas_size)
        self.offset = [0, 0]
        self.max_width = 0

    def addCube(self, source_image, size, offset):
        cube = Cube()
        cube.stretch(source_image, size, offset)
        self.max_width = max(self.max_width, cube.x * 2 + cube.z * 2)
        if self.offset[1] + cube.y + cube.z > self.atlas.shape[1]:
            self.offset = [self.max_width + self.offset[0], 0]
            self.max_width = 0
        cube.writeimage(self.atlas, self.offset)
        self.offset[1] += cube.z + cube.y
