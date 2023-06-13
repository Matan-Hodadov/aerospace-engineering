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


![image_detect_horizon_line](https://github.com/Matan-Hodadov/aerospace-engineering/assets/61780283/e37a26e1-ba74-49ec-9154-408b750def80)


## classify if an image is blurry or not:
big part of the satalite work is to take images of stars in space, but not all the images are in good quality, some of them can be blurry.
because of that we need a model that gets as an input an image and answer if it's blurry or not.


