
# First we will import the open cv package cv2 
import cv2 as cv
from PIL import Image
from PIL import ImageDraw

# Load the Cascade Classifiers xml files that "train" opencv on how to detect things on images.
# This time we are going to load 2 kinds of classifiers: One to detect faces and other to detect eyes
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Loading a face
img = cv.imread('floyd.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# The next step is to use the face_cascade classifier using detectMultiScale function. This function returns
# a list of objects as rectangles. The first parameter is an ndarray of the image.
faces = face_cascade.detectMultiScale(gray)
# And lets just print those faces out to the screen
rec=faces.tolist()[0]

pil_img=Image.fromarray(gray,mode="L")
# Setup our drawing context
drawing=ImageDraw.Draw(pil_img)
# And draw the new box
drawing.rectangle((rec[0],rec[1],rec[0]+rec[2],rec[1]+rec[3]), outline="white")
# And display
pil_img.show()

#######

def show_rects(faces):
    #Lets read in our gif and convert it
    pil_img=Image.open('msi_recruitment.gif').convert("RGB")
    # Set our drawing context
    drawing=ImageDraw.Draw(pil_img)
    # And plot all of the rectangles in faces
    for x,y,w,h in faces:
        drawing.rectangle((x,y,x+w,y+h), outline="white")
    #Finally lets display this
    pil_img.show()


pil_img=Image.open('msi_recruitment.gif')
open_cv_version=pil_img.convert("L")
open_cv_version.save("msi_recruitment.png")

cv_img=cv.imread('msi_recruitment.png')

cv_img_bin=cv.threshold(cv_img,120,255,cv.THRESH_BINARY)[1] # returns a list, we want the second value
# Now do the actual face detection
faces = face_cascade.detectMultiScale(cv_img_bin)
# Now lets see the results
show_rects(faces)

# The detectMultiScale() function from OpenCV also has a couple of parameters. The first of
# these is the scale factor. The scale factor changes the size of rectangles which are
# considered against the model, that is, the haarcascades XML file. You can think of it as if
# it were changing the size of the rectangles which are on the screen.
#
# Lets experiment with the scale factor. Usually it's a small value, lets try 1.05
faces = face_cascade.detectMultiScale(cv_img,1.05)
# Show those results
show_rects(faces)
# Now lets also try 1.15
faces = face_cascade.detectMultiScale(cv_img,1.15)
# Show those results
show_rects(faces)
# Finally lets also try 1.25
faces = face_cascade.detectMultiScale(cv_img,1.25)
# Show those results
show_rects(faces)