import cv2
import numpy as np
import matplotlib.pyplot as plt

# Corrected path
img= cv2.imread('1. Image Processing and Enhancement/image processing/Ganeshji.webp')

# Check if image loaded
if img is None:
    print("❌ Image not found! Check your file path.")
    exit()

image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

width, height = image_rgb.shape[1], image_rgb.shape[0]

tx, ty = 100, 70
translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

fig, axs = plt.subplots(1, 2, figsize=(7, 4))
axs[0].imshow(image_rgb), axs[0].set_title('Original Image')
axs[1].imshow(translated_image), axs[1].set_title('Image Translation')

for ax in axs:
    ax.set_xticks([]), ax.set_yticks([])

plt.tight_layout()
plt.show()