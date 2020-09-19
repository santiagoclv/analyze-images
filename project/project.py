from zipfile import ZipFile
from PIL import Image, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

def get_faces_sheet(faces, image_file):
    original_image = Image.open(image_file).convert("RGB")
    images = []
    new_size=(110,110)
    for x,y,w,h in faces:
        img = original_image.crop((x,y,x+w,y+h))
        images.append(img.resize(new_size, Image.BICUBIC))
    white_matrix=np.full((550, 110 * ((len(images) // 5) + 1) ),255,dtype=np.uint8)
    board = Image.fromarray(white_matrix,"L")
    for idx in range(len(images)):
        row = idx // 5
        column = idx % 5
        board.paste(images[idx], (column * 110, row * 110))
    return board

analized_pages = []

print('Wait while the images are processed...')

with ZipFile('readonly/small_img.zip') as image_zip:
    for image_name in image_zip.namelist():
        with image_zip.open(image_name) as image_file:
            pic = Image.open(image_file).convert("L")
            imgae_array = np.array(pic)
            th = cv.threshold(imgae_array,180,255,cv.THRESH_BINARY)[1]
            faces_zones = face_cascade.detectMultiScale(th, 1.10)
            faces_sheet = get_faces_sheet(faces_zones, image_file)
            text=pytesseract.image_to_string(pic, lang = 'eng')
            text=text.lower()
            analized_pages.append({"faces": faces_sheet, "text": text, "image_name": image_name})

while True:
    input_message =   '''Enter a word to look up for, or 'quit':'''
    response = input(input_message)

    if response != "quit":
        print('Results found for word ${} \n').format(response)
        for page in analized_pages:
            if response in page["text"]:
                print('Results found in file ${} \n').format(page["image_name"])
                display(page["faces"])
            else:
                print('No results found in file ${} \n').format(page["image_name"])
    else: 
        break