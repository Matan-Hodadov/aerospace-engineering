import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, datasets

def detect_horizon(img):
    image_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_blurred = cv2.GaussianBlur(image_grayscale, ksize=(3, 3), sigmaX=0)
    _, image_thresholded = cv2.threshold(image_blurred, thresh=0, maxval=1,type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    image_thresholded = image_thresholded - 1
    image_closed = cv2.morphologyEx(image_thresholded, cv2.MORPH_CLOSE,kernel=np.ones((9, 9), np.uint8))
    img_with_horizon_detected = cv2.Canny(image=image_closed, threshold1=100, threshold2=200)
    x=[]
    y=[]
    xx=[]
    for i in range(img_with_horizon_detected.shape[0]):
        for j in range(img_with_horizon_detected.shape[1]):
            if img_with_horizon_detected[i][j]!=0:
                xx.append(j)
                x.append([j])
                y.append([i])
    ransac = linear_model.RANSACRegressor()
    ransac.fit(x, y)
    inlier_mask = ransac.inlier_mask_
    outlier_mask = np.logical_not(inlier_mask)
    line_x=[[min(xx)],[max(xx)]]
    line_y=ransac.predict(line_x)
    line_x=[line_x[0][0],line_x[1][0]]
    line_y=[line_y[0][0],line_y[1][0]]
    p1=[line_x[0],line_y[0]]
    p2=[line_x[1],line_y[1]]
    m=(p2[1]-p1[1])/(p2[0]-p1[0])
    b=p1[1]-p1[0]*m
    x1,x2,y1,y2=0,0,0,0
    if b<0 or b>img_with_horizon_detected.shape[0]:
        y1=0
        y2=img_with_horizon_detected.shape[0]
        x1=(y1-b)/m
        x2 = (y2 - b) / m
    else:
        x1=0
        x2=img_with_horizon_detected.shape[1]
        y1=x1*m+b
        y2=x2*m+b
    line_x = [x1, x2]
    line_y = [y1, y2]


    return image_thresholded, image_closed ,img_with_horizon_detected,line_x,line_y






if __name__ == '__main__':
    #main2()
    fig, axes = plt.subplots(2, 4)
    image = cv2.imread("image2.jpg")
    axes[0][0].imshow(image)

    axes[0][0].axis('off')
    axes[0][0].set_title('Original Image')


    img1,img2,img_with_horizon_detected,line_x,line_y = detect_horizon(image)
    axes[0][0].plot(line_x, line_y, color="red", linewidth=2)
    axes[0][1].imshow(img1)
    axes[0][1].axis('off')

    axes[0][2].imshow(img2)
    axes[0][2].axis('off')

    axes[0][3].imshow(img_with_horizon_detected)
    axes[0][3].axis('off')
    axes[0][3].set_title('detect horizon line')

    image = cv2.imread("image1.jpg")
    axes[1][0].imshow(image)
    axes[1][0].axis('off')
    axes[1][0].set_title('Original Image')

    img1,img2,img_with_horizon_detected,line_x,line_y = detect_horizon(image)
    axes[1][0].plot(line_x, line_y, color="red", linewidth=2)
    axes[1][1].imshow(img1)
    axes[1][1].axis('off')

    axes[1][2].imshow(img2)
    axes[1][2].axis('off')
    axes[1][3].imshow(img_with_horizon_detected)
    axes[1][3].axis('off')
    axes[1][3].set_title('detect horizon line')
    plt.show()







