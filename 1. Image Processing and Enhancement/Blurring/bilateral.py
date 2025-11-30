import cv2
import matplotlib.pyplot as plt 

image_path = '1. Image Processing and Enhancement/dog-cats.webp'

image = cv2.imread(image_path)
image_resized = cv2.resize(image, (1900,800))

bilateral = cv2.bilateralFilter(image_resized,15,150,150)
bilateral_rgb = cv2.cvtColor(bilateral,cv2.COLOR_BGR2RGB)
plt.imshow(bilateral_rgb)
plt.title('Bilateral Blurred Image')
plt.axis('off')
plt.show()