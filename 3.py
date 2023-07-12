import cv2

import numpy as np
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=1)
edge_image = cv2.absdiff(image, eroded_image)
cv2.imshow("Original Image", image) 
cv2.imshow("Edge Image (Erosion)", edge_image)
dilated_image = cv2.dilate(image, kernel, iterations=1)
edge_image_dilation = cv2.absdiff(image, dilated_image)
cv2.imshow("Edge Image (Dilation)", edge_image_dilation)
cv2.waitKey(0)