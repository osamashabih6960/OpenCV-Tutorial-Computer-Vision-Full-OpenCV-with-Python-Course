import cv2

img = cv.imread('1. Image Processing and Enhancement\Grayscaling of Images\Tomatoes.png')
rows,cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        gray = (img[i,j,0] + img[i,j,1] + img[i,j,2])/3
        img[i,j] = [gray,gray,gray]
        
cv2.imshow('Grayscale Image (Average)' ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()

