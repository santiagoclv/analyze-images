from PIL import Image
import pytesseract
import string

image=Image.open('storefront.jpg')

bounding_box=(900, 420, 940, 445)
little_sign=image.crop(bounding_box)
new_size=(little_sign.width*10,little_sign.height*10)

bigger_sign=little_sign.resize(new_size, Image.BICUBIC)

def binarize(image_to_transform, threshold):
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))< threshold:
                output_image.putpixel( (x,y), 0 )
            else:
                output_image.putpixel( (x,y), 255 )
    return output_image

eng_dict=[]
with open ("words_alpha.txt", "r") as f:
    data=f.read()
    eng_dict=data.split("\n")

for i in range(150,170):
    strng=pytesseract.image_to_string(binarize(bigger_sign,i))
    strng=strng.lower()
    comparison=''
    for character in strng:
        if character in string.ascii_lowercase:
            comparison=comparison+character
    if comparison in eng_dict:
        print(comparison)