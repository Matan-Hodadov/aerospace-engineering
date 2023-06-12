import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import cv2
import os
import pathlib


def var(image):
    return int(ndimage.variance(image))


dataset_name = 'good_image_dataset'
window_len = 20
variance_threshold = 300

# path
current_directory = os.getcwd()
current_directory += '\\' + dataset_name
images = os.listdir(current_directory)
for image_name in images:
    image = cv2.imread(dataset_name+'/'+image_name)
    laplacian_image = cv2.Laplacian(image, cv2.CV_64F)
    if var(image) < var(laplacian_image):
        continue
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

    print("--------------------------------------------------------------------------")
    print(image_name)
    print("image var:", var(image))
    print("laplacian image var:", var(laplacian_image))
    print("image window var:", var_sum//window_num)
    print("laplacian image window var:", laplacian_var_sum//window_num)

