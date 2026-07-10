import cv2
import numpy as np
from cube import Cube

example = cv2.imread("res/example.png")

# example values
atlas = np.zeros((32, 32, 3))
cube = Cube()
cube.stretch(example, [4, 8, 6], [2, 4])
cube.writeimage(atlas, [3,3])

cv2.imwrite("res/example_copy.png", atlas)