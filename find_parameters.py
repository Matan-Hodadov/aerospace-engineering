import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import cv2
import os
import pathlib


def var(image):
    return int(ndimage.variance(image))


current_directory = os.getcwd()
dataset_name = 'good_image_dataset'
current_directory += '\\' + dataset_name
images = os.listdir(current_directory)

images_num = len(images)

for window_len in range(5, 41, 5):
    for variance_threshold in range(25, 401, 25):
        diff = []
        images.reverse()
        vals = []
        for image_name in images:
            image = cv2.imread(dataset_name + '/' + image_name)
            laplacian_image = cv2.Laplacian(image, cv2.CV_64F)
            if var(image) < var(laplacian_image):
                images_num -= 1
                continue
            else:
                laplacian_var_sum = 0
                window_num = 0
                width = image.shape[0]
                height = image.shape[1]
                for i in range(0, height, window_len):
                    for j in range(0, width, window_len):
                        laplacian_window = laplacian_image[j:j+window_len, i:i+window_len, :]

                        if var(laplacian_window) < variance_threshold:
                            continue
                        laplacian_var_sum += var(laplacian_window)
                        window_num += 1
                vals.append(laplacian_var_sum//window_num)
        if len(vals) != images_num:
            continue

        # IMPORTANT!
        # It is important to know the type of pictures you have before you start using the vals
        # in order to find the best parameters
        # in our data we have 4 pictures (very bad one, kind of bad, better pic but still not good,
        # and a very good image)

        # You can put only good images to see the results of good images. The same goes for bad images
        # You can also put a pair of very good and very bad images and check their differences

        # In our data we want as much spread as possible and that the last val will be the smallest as can be
        # This is why we calculated the differences and then multiply the last one by 1 and then sum
        for inx in range(images_num-1):
            vals[inx] = vals[inx]-vals[inx+1]
        vals[-1] = -1 * vals[-1]
        diff.append(sum(vals))

        print("window len:", window_len, "threshold:", variance_threshold, "diff is:", diff[-1])
diff.sort()
print("biggest diff is:", diff[-1])




