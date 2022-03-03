from PIL import ImageFont, ImageDraw, Image, ImageOps
import cv2
import math
import numpy as np

# Image to Put Coordinates Size
print("Loading Image...")
offset = (720, 540)
img = cv2.imread("nftRaw.png") # 512x512
img_shape = img.shape
print("Image loaded successfully.")

# Environment Setup
cv2_im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
mainImage = Image.fromarray(cv2_im_rgb) 
imW, imH = mainImage.size
draw = ImageDraw.Draw(mainImage)  

verticalLines = Image.open("verticalLine.png") # This file should have the same vertical pixels size as the main image
horizontalLines = Image.open("horizontalLine.png") # Ibidem but with horizontal pixels.


verticalPortions = int(math.ceil( imW / offset[0] )) 
horizontalPortions = int(math.ceil( imH / offset[1] )) 
print(verticalPortions, horizontalPortions)

# Creation of map with coordinates.
# Vertical Lines
print("Vertical Lines.")
for j in range(verticalPortions):
        currentX = round(offset[0] * j)
        currentY = 0
        currentCoord = (currentX, currentY)

        mainImage = mainImage.copy()
        mainImage.paste(verticalLines, currentCoord, mask = verticalLines)
        print("Generated vertical line N°: " + str(j))

print("Horizontal Lines.")
for i in range(horizontalPortions):
        currentX = 0
        currentY = round(offset[1] * i)
        currentCoord = (currentX, currentY)

        mainImage = mainImage.copy()
        mainImage.paste(horizontalLines, currentCoord, mask = horizontalLines)

        print("Generated horizontal line N°: " + str(i))
mainImage = mainImage.save("mainWithCoordinates.png")

print("Process completed.")