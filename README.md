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
![image_detect_horizon_line](https://github.com/Matan-Hodadov/aerospace-engineering/assets/61780283/e37a26e1-ba74-49ec-9154-408b750def80)


## classify if an image is blurry or not:
big part of the satalite work is to take images of stars in space, but not all the images are in good quality, some of them can be blurry.
because of that we need a model that gets as an input an image and answer if it's blurry or not.


