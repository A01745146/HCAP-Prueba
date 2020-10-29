import cv2
import numpy as np

imagen=cv2.imread("imagen.jpg")
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
print(imagen.shape)

print(imagen[0][0])

imagen=cv2.resize(imagen,(256,256))

imagen=cv2.imread("imagen.jpg")
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
print(imagen.shape)
print(imagen[0][0])

imagen[0][0]=0
imagen[0][1]=1
imagen[0][2]=2

cv2.imwrite("grayimagen.jpg",imagen)

matriz=np.zeros((256,256),np.float32)
print(matriz.shape)
cv2.imwrite("matrizimagen.jpg",matriz)
imagen=cv2.cvtColor(matriz,cv2.COLOR_GRAY2BGR)
print(imagen.shape)
cv2.imwrite("matrizcolorimagen.jpg",imagen)

#cv2.imwrite("resizeimagen.jpg",imagen)
#cv2.imshow("image",imagen)
#cv2.waitKey(0)
