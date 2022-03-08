import cv2
import numpy as np
import matplotlib.pyplot as plt

#Lendo a imagem e exibindo
img = cv2.imread('gato.png')
cv2.imshow('Original',img)
cv2.waitKey()
   
#Transformando a imagem em escala de cinza e exibindo
img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
cv2.imshow('Imagem em escala de cinza', img_cinza)
cv2.waitKey()
