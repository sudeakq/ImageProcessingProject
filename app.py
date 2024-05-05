import cv2
from matplotlib import pyplot as plt
import numpy as np


img_path = "images/1_xBb9dtIT9N4QmZInvHtUWg.webp"
img = cv2.imread(img_path)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image)
plt.show()
print(gray_image.shape)