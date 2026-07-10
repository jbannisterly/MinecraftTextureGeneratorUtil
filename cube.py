import cv2
import numpy as np

class Cube:
    def __init__(self):
        self.left = np.array([[[]]])
        self.right = np.array([[[]]])
        self.up = np.array([[[]]])
        self.down = np.array([[[]]])
        self.forward = np.array([[[]]])
        self.backward = np.array([[[]]])
        self.x = 0
        self.y = 0
        self.z = 0
    
    def writeimage(self, image, offset):
        image[offset[1] + self.z * 0 + self.y * 0: offset[1] + self.z * 1 + self.y * 0, offset[0] + self.z * 1 + self.x * 0: offset[0] + self.z * 1 + self.x * 1, :] = self.up
        image[offset[1] + self.z * 0 + self.y * 0: offset[1] + self.z * 1 + self.y * 0, offset[0] + self.z * 1 + self.x * 1: offset[0] + self.z * 1 + self.x * 2, :] = self.down
        image[offset[1] + self.z * 1 + self.y * 0: offset[1] + self.z * 1 + self.y * 1, offset[0] + self.z * 0 + self.x * 0: offset[0] + self.z * 1 + self.x * 0, :] = self.right
        image[offset[1] + self.z * 1 + self.y * 0: offset[1] + self.z * 1 + self.y * 1, offset[0] + self.z * 1 + self.x * 0: offset[0] + self.z * 1 + self.x * 1, :] = self.forward
        image[offset[1] + self.z * 1 + self.y * 0: offset[1] + self.z * 1 + self.y * 1, offset[0] + self.z * 1 + self.x * 1: offset[0] + self.z * 2 + self.x * 1, :] = self.left
        image[offset[1] + self.z * 1 + self.y * 0: offset[1] + self.z * 1 + self.y * 1, offset[0] + self.z * 2 + self.x * 1: offset[0] + self.z * 2 + self.x * 2, :] = self.backward
        
    def stretch(self, image, size, offset):
        self.x = size[0]
        self.y = size[1]
        self.z = size[2]
        self.forward = image[offset[1]:offset[1] + self.y, offset[0]:offset[0] + self.x, :].copy()
        self.backward = self.forward[:, ::-1, :].copy()
        self.up = np.tile(self.forward[0:1, :, :], (self.z, 1, 1))
        self.down = np.tile(self.forward[-1:, :, :], (self.z, 1, 1))
        self.right = np.tile(self.forward[:, 0:1, :], (1, self.z, 1))
        self.left = np.tile(self.forward[:, -1:, :], (1, self.z, 1))



example = cv2.imread("res/example.png")

# example values
atlas = np.zeros((32, 32, 3))
cube = Cube()
cube.stretch(example, [8, 4, 6], [2, 4])
cube.writeimage(atlas, [3,3])

cv2.imwrite("res/example_copy.png", atlas)