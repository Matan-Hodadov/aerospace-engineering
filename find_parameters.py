import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import cv2
import os
import pathlib


def var(image):
    return int(ndimage.variance(image))


image_name = 'blurred_image.jpg'
image = cv2.imread('good_image_dataset/'+image_name)
laplacian_image = cv2.Laplacian(image, cv2.CV_64F)
for window_len in range(5, 41, 5):
    for variance_threshold in range(0, 501, 25):
        if var(image) < var(laplacian_image):
            continue
        else:
            var_sum = 0
            laplacian_var_sum = 0
            window_num = 0
            width = image.shape[0]
            height = image.shape[1]
            for i in range(0, height, window_len):
                for j in range(0, width, window_len):
                    window = image[j:j+window_len, i:i+window_len, :]
                    laplacian_window = laplacian_image[j:j+window_len, i:i+window_len, :]

                    if var(laplacian_window) < variance_threshold:
                        continue
                    var_sum += var(window)
                    laplacian_var_sum += var(laplacian_window)
                    window_num += 1

        print("window len:", window_len, "threshold:", variance_threshold, "var is:", laplacian_var_sum//window_num)

            # print("--------------------------------------------------------------------------")
            # print(image_name)
            # print("image var:", var(image))
            # print("laplacian image var:", var(laplacian_image))
            # print("image window var:", var_sum//window_num)
            # print("laplacian image window var:", laplacian_var_sum//window_num)



