import cv2
import numpy as np
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
edge_x = cv2.filter2D(image, -1, sobel_x) 
edge_y = cv2.filter2D(image, -1, sobel_y)
cv2.imshow('Sobel X', edge_x) 
cv2.imshow('Sobel Y', edge_y)
texture = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
texture_image = cv2.filter2D(image, -1, texture)
cv2.imshow('Texture', texture_image)
cv2.waitKey(0)
cv2.destroyAllWindows()