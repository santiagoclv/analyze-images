from PIL import Image, ImageDraw, ImageFont

text = "Hola maadafaker"
base = Image.open("msi_recruitment.gif").convert("RGBA")

# # make a blank image for the text, initialized to transparent text color
# 
# get a font
fnt = ImageFont.truetype("fanwood-webfont.ttf", 75)
# mesure text size
size = fnt.getsize(text)
new_size = (size[0] + 20, size[1] + 20)
txt = Image.new("RGBA", new_size, (0, 0, 0))
# # get a drawing context
d = ImageDraw.Draw(txt)

# # draw text, half opacity
d.text((10,10), text, font=fnt, fill=(255,255,255), align="center")

txt.show()



# base = Image.open("cobrakai.jpg").convert("RGBA")
# base_2 = Image.open("download.jpg").convert("RGBA")


# ImageChops.darker(base, base_2).show() # super cool effects!