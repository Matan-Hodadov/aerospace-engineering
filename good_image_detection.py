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


# var_temp = []
# lapl_temp = []


# path
current_directory = os.getcwd()
current_directory += '\\' + dataset_name
images = os.listdir(current_directory)
for image_name in images:
    image = cv2.imread(dataset_name+'/'+image_name)
    laplacian_image = cv2.Laplacian(image, cv2.CV_64F)
    if var(image) < var(laplacian_image):
        continue
    # print(image1.shape)
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

            # var_temp.append(var(window))
            # lapl_temp.append((var(laplacian_window)))

    # var_temp.sort()
    # lapl_temp.sort()

    # fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    # axs[0].hist(var_temp, ec='black', bins=10)
    # axs[1].hist(lapl_temp, ec='black', bins=10)
    # plt.show()

    print("--------------------------------------------------------------------------")
    print(image_name)
    print("image var:", var(image))
    print("laplacian image var:", var(laplacian_image))
    print("image window var:", var_sum//window_num)
    print("laplacian image window var:", laplacian_var_sum//window_num)


# # background images
# image1 = cv2.imread("image1.jpg")
# image1_var = int(ndimage.variance(image1))
# image2 = cv2.imread("image2.jpg")
# image2_var = int(ndimage.variance(image2))
# blurred_image1 = cv2.imread("blurred_image1.jpg")
# blurred_image1_var = int(ndimage.variance(blurred_image1))
# # blurred_image2 = cv2.imread("blurred_image2.jpg")
# # blurred_image2_var = int(ndimage.variance(blurred_image2))
# # blurred_image3 = cv2.imread("blurred_image3.jpg")
# # blurred_image3_var = int(ndimage.variance(blurred_image3))
#
# print("background")
# print("all image variance")
# print(image1_var)
# print(image2_var)
# print("blurred -", blurred_image1_var)
#
# print("laplacian")
# print(int(cv2.Laplacian(image1, cv2.CV_64F).var()))
# print(int(cv2.Laplacian(image2, cv2.CV_64F).var()))
# print("blurred -", int(cv2.Laplacian(blurred_image1, cv2.CV_64F).var()))
# print()
# #
# # plt.figure()
# # plt.title("variance = " + str(image1_var))
# # plt.imshow(image1)
# # plt.show()
# #
# # plt.title("variance = " + str(blurred_image1_var))
# # plt.imshow(blurred_image1)
# # plt.show()
# #
# # plt.title("variance = " + str(image2_var))
# # plt.imshow(image2)
# # plt.show()
# #
# # plt.title("variance = " + str(blurred_image2_var))
# # plt.imshow(blurred_image2)
# # plt.show()
# #
# # star images
# star_image = cv2.imread("star_image.jpg")
# star_image_var = int(ndimage.variance(star_image))
# # star_image2_var = int(ndimage.variance(star_image))
# blurred_star_image = cv2.imread("blurred_star_image.jpg")
# blurred_star_image_Var = int(ndimage.variance(blurred_star_image))
# # blurred_star_image2 = cv2.imread("blurred_star_image2.jpg")
# # blurred_star_image2_Var = int(ndimage.variance(blurred_star_image2))
#
# print("stars")
# print("all image var")
# print(star_image_var)
# print("blurred -", blurred_star_image_Var)
#
# print("laplacian")
# print(int(cv2.Laplacian(star_image, cv2.CV_64F).var()))
# print("blurred -", int(cv2.Laplacian(blurred_star_image, cv2.CV_64F).var()))
# # print(blurred_star_image2_Var)
# # print(cv2.Laplacian(blurred_star_image2, cv2.CV_64F).var())
# #
# plt.title("variance = " + str(int(cv2.Laplacian(star_image, cv2.CV_64F).var())))
# plt.imshow(star_image)
# plt.show()
#
# # plt.title("variance = " + str(blurred_star_image_Var))
# plt.title("variance = 127")
# plt.imshow(blurred_star_image)
# plt.show()
# #
# # plt.title("variance = " + str(blurred_star_image2_Var))
# # plt.imshow(blurred_star_image2)
# # plt.show()


