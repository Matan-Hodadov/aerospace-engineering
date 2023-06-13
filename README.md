# aerospace-engineering
in this project we tried to solve two different problems:
## detect horizon line in an image:
in some cases the satalite needs to know the orientention between itself and earth and he does it by detcting the horizon line and calculating the 
angle of the line compared to the satalite.
in the detect_horizon.py file we have function that get as an input image of earth(part of it) in space and as an output you get the images that describes the work flow to detect the horizon line and in addition return two points that creates the line of the horizon.

the work flow of the algorithm to detect the horizon line:

1.get the original image

2.convert the original image to gray_scale

3.blurr the image

4.compute a histogram of intenseties of all the pixels in the blured image. because the image contains 2 main parts:the earth and space, then the histogram will contain two main gaussian distributions like this:



![histogram](https://github.com/Matan-Hodadov/aerospace-engineering/assets/61780283/d0b4433e-d893-4cda-ac00-e6e08c1b44b3)

then we need to find the best intensity value threshold that seperate those two distributions.

5. we check every pixel in the image, if his intensity is greater then the threshold then we give it value 1, else 0.

6. now we can preform canny edge detection and detect the pixels of the horizon line.

7. we get all the coardinates of the pixels of the horizon line and train a RANSAC model to fit the best line to those points.

8.return images of the horizon line and two points that creates the horizon line.

the red line in the original images is the line we found with the RANSAC algorithm.


![image_detect_horizon_line](https://github.com/Matan-Hodadov/aerospace-engineering/assets/61780283/e37a26e1-ba74-49ec-9154-408b750def80)


## classify if an image is blurry or not:
big part of the satalite work is to take images of stars in space, but not all the images are in good quality, some of them can be blurry.
because of that we need a model that gets as an input an image and answer if it's blurry or not.
<br/>
One common method for this problem is using laplacian transform on the image
<br/>
<img width="64" alt="laplacian" src="https://github.com/Matan-Hodadov/aerospace-engineering/assets/59831698/0b70744b-b605-4d71-a61c-f99b5b4677dd">
<br/>
and then calculating the variance of the entire picture (calculating the variance of each pixel compared to the entire picture)
<br/><br/>
However, this method wont be good enough for our needs bacause in space images (and especially stars images) even blurry images can give high variance due to the fact that most of the pixals are either black or white (stars will be white and all the other pixels will be black or at least close)
<br/>
Our solution for this problem is by using windows. We split the picture into windows in the same size and calculating the variance of each pixal compared to the window that he is in. This gives of the variance of a pixal compared to this close pixals only! and by that gives us better results for detecting good and blurry stars from space images
<br/>
Each user can change the model parameters to work better with his own style of images
<br/><br/>
Here is some results: 
<br/>
![Figure_1](https://github.com/Matan-Hodadov/aerospace-engineering/assets/59831698/4469342c-52ad-4472-8a87-5a1120a7c126)
<br/>
![Figure_4](https://github.com/Matan-Hodadov/aerospace-engineering/assets/59831698/1cc992e9-0e16-48c0-9486-7c9dfa62db16)


