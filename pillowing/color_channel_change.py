from PIL import Image, ImageDraw, ImageFont

def get_changeed_intesity_over_channel(image, channel=0, intesity=1):
    rr, gg, bb = image.split()
    lam = lambda channel_selected: lambda p: p * intesity if channel == channel_selected else p
    rr = rr.point(lam(0))
    gg = gg.point(lam(1))
    bb = bb.point(lam(2))
    image_modified = Image.merge("RGB", (rr, gg, bb))

    fnt = ImageFont.truetype("fanwood-webfont.ttf", 75)
    get_text = lambda t: 'Channel {}, intensity {}'.format(t[0], t[1])
    text = get_text((channel, intesity))
    text_size  = fnt.getsize(text)
    text_image = Image.new("RGBA", (image.width, text_size[1] + 20), (0, 0, 0))
    d = ImageDraw.Draw(text_image)
    d.text((10,10), text, font=fnt, fill=(255,255,255), align="center")

    board = Image.new(image.mode, (image.width , image.height + text_size[1] + 20))
    board.paste(image_modified, (0, 0) )
    board.paste(text_image, (0, image.height) )
    return board
    

image=Image.open("msi_recruitment.gif")
image=image.convert('RGB')

images=[]
for channel in range(3):
    for intesity in [0.1, 0.5, 0.9]:
        images.append(get_changeed_intesity_over_channel(image, channel=channel, intesity=intesity))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet= Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save("channel_intensity_thing.png","PNG")