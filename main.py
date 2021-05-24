
import cv2
from matplotlib import pyplot as plt
# read image as grey scale
img = cv2.imread('flower.jpg')

# get image height, width
(h, w) = img.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0

# Perform the counter clockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

# 180 degrees
M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w, h))

# 270 degrees
M = cv2.getRotationMatrix2D(center, angle270, scale)
rotatedtrai90 = cv2.warpAffine(img, M, (h, w))
images = [img, rotated90, rotated180 ,rotatedtrai90]
titles = ['Anh goc', 'Xoay trai', 'xoay 180','Xoay phai']
for i in range(4):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()