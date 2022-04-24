import cv2
import numpy as np


# sıfırlar 0 beyazlar 1 olarak kabul edilir ve iki resim mantıksal olarak ilgili operator (and or vs..) toplanır
img1 = cv2.imread('bitwise_1.png')
img2 = cv2.imread('bitwise_2.png')

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img2, img1)
bit_not_img1 = cv2.bitwise_not(img1)
bit_not_img2 = cv2.bitwise_not  (img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bit_and', bit_and)
cv2.imshow('bit_or', bit_or)
cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_not_img1', bit_not_img1)
cv2.imshow('bit_not_img2', bit_not_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
