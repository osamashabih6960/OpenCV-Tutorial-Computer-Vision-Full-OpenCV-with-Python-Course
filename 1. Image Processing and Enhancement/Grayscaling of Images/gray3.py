import cv2 
img_wighted = cv2.imread('1. Image Processing and Enhancement\Grayscaling of Images\Tomatoes.png')
rows, cols = img_wighted.shape[:2]

for i in range(rows):
    for j in range(cols):
        gray = 0.2989 * img_wighted[i,j][2] + 0.5870 * img_wighted[i,j][1]+ 0.1140 * img_wighted[i,j][0]
        img_wighted[i,j] = [gray, gray, gray]
        
cv2.imshow('Grayscale Image (Weighted)', img_wighted)
cv2.WaitKey(0)
cv2.destroyAllWindows()

