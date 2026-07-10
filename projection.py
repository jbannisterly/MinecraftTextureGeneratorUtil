import cv2

example = cv2.imread("res/example.png")
print(example.shape)
cv2.imwrite("res/example_copy.png", example)