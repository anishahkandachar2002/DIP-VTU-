import cv2
import numpy as np
image = cv2.imread("image.jpg")
height, width = image.shape[:2]
scale = 2
dx = 50 
dy = -100
angle = 45
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
translated_image = cv2.warpAffine(rotated_image, translation_matrix, (width, height))
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Scaled Image", cv2.resize(image, None, fx=scale, fy=scale)) 
cv2.imshow("Translated Image", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()