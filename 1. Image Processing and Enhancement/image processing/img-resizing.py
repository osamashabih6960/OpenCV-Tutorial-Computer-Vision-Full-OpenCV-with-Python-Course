import cv2
import numpy as np
import matplotlib.pyplot as plt

# Corrected path
image = cv2.imread('1. Image Processing and Enhancement/image processing/Ganeshji.webp')

# Check if image loaded
if image is None:
    print("❌ Image not found! Check your file path.")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

scale_factor_1 = 3.0  
scale_factor_2 = 1/3.0

height, width = image_rgb.shape[:2]

new_height = int(height * scale_factor_1)
new_width = int(width * scale_factor_1)

zoomed_image = cv2.resize(
    src=image_rgb, 
    dsize=(new_width, new_height), 
    interpolation=cv2.INTER_CUBIC
)

new_height1 = int(height * scale_factor_2)
new_width1 = int(width * scale_factor_2)

scaled_image = cv2.resize(
    src=image_rgb, 
    dsize=(new_width1, new_height1), 
    interpolation=cv2.INTER_AREA
)

fig, axs = plt.subplots(1, 3, figsize=(10, 4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image Shape: ' + str(image_rgb.shape))
axs[1].imshow(zoomed_image)
axs[1].set_title('Zoomed Image Shape: ' + str(zoomed_image.shape))
axs[2].imshow(scaled_image)
axs[2].set_title('Scaled Image Shape: ' + str(scaled_image.shape))

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

