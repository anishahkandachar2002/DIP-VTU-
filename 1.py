import cv2
image = cv2.imread("image.jpg")
height, width = image.shape[:2]
up_left = image[0:height//2, 0:width//2] 
up_right = image[0:height//2, width//2:width] 
down_left = image[height//2:height, 0:width//2]
down_right = image[height//2:height, width//2:width]
cv2.imshow("Up Left", up_left)
cv2.imshow("Up Right", up_right)
cv2.imshow("Down Left", down_left)
cv2.imshow("Down Right", down_right)
cv2.waitKey(0)
