{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c841857b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "#Lendo a imagem e exibindo\n",
    "img = cv2.imread('gato.png')\n",
    "cv2.imshow('Original',img)\n",
    "cv2.waitKey()\n",
    "\n",
    "\n",
    "#Transformando a imagem em escala de cinza e exibindo\n",
    "img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)\n",
    "\n",
    "cv2.imshow('Imagem em escala de cinza', img_cinza)\n",
    "cv2.waitKey()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c59b1fbc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
