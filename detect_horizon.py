import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib


def detect_horizon(img):
    image_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_blurred = cv2.GaussianBlur(image_grayscale, ksize=(3, 3), sigmaX=0)
    _, image_thresholded = cv2.threshold(image_blurred, thresh=0, maxval=1, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    image_thresholded = image_thresholded - 1
    image_closed = cv2.morphologyEx(image_thresholded, cv2.MORPH_CLOSE,kernel=np.ones((9, 9), np.uint8))
    img_with_horizon_detected = cv2.Canny(image=image_closed, threshold1=100, threshold2=200)
    return image_thresholded, image_closed, img_with_horizon_detected


if __name__ == '__main__':
    path = 'horizon_dataset/'
    fig, axes = plt.subplots(2, 4)
    image = cv2.imread(path+"image2.jpg")
    axes[0][0].imshow(image)
    axes[0][0].axis('off')
    axes[0][0].set_title('Original Image')

    img1, img2, img_with_horizon_detected = detect_horizon(image)
    axes[0][1].imshow(img1)
    axes[0][1].axis('off')

    axes[0][2].imshow(img2)
    axes[0][2].axis('off')

    axes[0][3].imshow(img_with_horizon_detected)
    axes[0][3].axis('off')
    axes[0][3].set_title('detect horizon line')

    image = cv2.imread(path+"image1.jpg")
    axes[1][0].imshow(image)
    axes[1][0].axis('off')
    axes[1][0].set_title('Original Image')

    img1, img2, img_with_horizon_detected = detect_horizon(image)
    axes[1][1].imshow(img1)
    axes[1][1].axis('off')

    axes[1][2].imshow(img2)
    axes[1][2].axis('off')
    axes[1][3].imshow(img_with_horizon_detected)
    axes[1][3].axis('off')
    axes[1][3].set_title('detect horizon line')
    plt.show()







