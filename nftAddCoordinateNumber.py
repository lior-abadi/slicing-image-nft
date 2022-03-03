from PIL import ImageFont, ImageDraw, Image, ImageOps
import cv2
import math
import numpy as np

# Image to Put Coordinates Size
print("Loading Image...")
offset = (720, 540)
img = cv2.imread("mainWithCoordinates.png")
print("Image loaded successfully.")

# Environment Setup
cv2_im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
mainImage = Image.fromarray(cv2_im_rgb) 
imW, imH = mainImage.size
draw = ImageDraw.Draw(mainImage)  

fontSize = 500  # Edit the font and its size if you need it.
font = ImageFont.truetype(font= r"./latoFont/Lato-Bold.ttf", size = fontSize)

verticalPortions = int(math.ceil( imW / offset[0] )) 
horizontalPortions = int(math.ceil( imH / offset[1] )) 


# Vertical Coordinates
print("Vertical Coordinates.")
for j in range(0, verticalPortions):
    print("Generating number: " + str(j))
    text = str(j-1)
    if (j >= 10) :
        adjustmentFactor = 0.8
    else:
        adjustmentFactor = 0.6
    
    textsize = draw.textsize(text, font)
    textX = round(  (offset[0]) * (j - adjustmentFactor))
    textY = round((offset[1] - textsize[1]) / 2)
    draw.text((textX, textY), text, font= font, fill=(0,0,0,255)) 

print("Horizontal Coordinates.")
for i in range(0, horizontalPortions):
     
    if(i == 0):
        continue

    print("Generating number: " + str(i)) 

    text = str(i)

    if (i >= 10):
        adjustmentYFactor = 0.85
        adjustmentXFactor = 0.8
    else:
        adjustmentYFactor = 0.85
        adjustmentXFactor = 0.6 
    
    textsize = draw.textsize(text, font)
    textX = round(  (offset[0]) * (1 - adjustmentXFactor))
    textY = round(  (offset[1]) * (i+1 - adjustmentYFactor))

    draw.text((textX, textY), text, font= font, fill=(0,0,0,255)) 

mainImage = mainImage.save("finishedMap.png")
print("Process completed.")