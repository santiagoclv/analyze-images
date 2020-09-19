
# First we will import the open cv package cv2 
import cv2 as cv
import numpy as np
from PIL import Image
import inspect

from PIL import Image
# We'll load the floyd.jpg image 
img = cv.imread('floyd.jpg')
# And we'll convert it to grayscale using the cvtColor image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


inspect.getmro(type(gray))

image = Image.fromarray(gray, "L")

single_dim = np.array([25, 50 , 25, 10, 10])
double_dim = np.array([single_dim])
double_dim
# a simple line of 5 pixels
Image.fromarray(double_dim, "L").show()
# height and width the matrix
double_dim.shape
# height and width the image, plus its depth
img.shape
# see in detail how a pixel is with this depth
first_pixel=img[0][0]
first_pixel

# It is posible to reshap a matrix or image

print("Original image")
print(gray)
# If we wanted to represent that as a one dimensional image, we just call reshape
print("New image")
# And reshape takes the image as the first parameter, and a new shape as the second
image1d=np.reshape(gray,(1,gray.shape[0]*gray.shape[1]))
print(image1d)




###
### Also it is very easy to process and manipulate an image using matrixes
###

# We'll load the 2 column image
img = cv.imread('readonly/two_col.png')
# And we'll convert it to grayscale using the cvtColor image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# this is a way to take a portion of a matrix
gray[2:4,1:3]


# One that we want to consider in this case is count_nonzero(), which just returns
# the number of entries in the matrix which are not zero.
np.count_nonzero(gray[2:4,1:3])
# This is an exellent way to see if a portion of the images has some black or not in it


# It's easy also to create matrix with 1 byte per place (np.uint8)
white_matrix=np.full((12,12),255,dtype=np.uint8)
display(Image.fromarray(white_matrix,"L"))
white_matrix
# looks pretty boring, it's just a giant white square we can't see. But if we want, we can
# easily color a column to be black
# This is an excellent way to create some noice to make it easy and faster than 
# the krakening script to find out the lines of text
white_matrix[:,6]=np.full((1,12),0,dtype=np.uint8)
display(Image.fromarray(white_matrix,"L"))
white_matrix