from turtle import color
import cv2
import os
import math
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageOps
import json

# Font and placement Edit
fontSize = 55
fontRoute = r"./latoFont/Lato-Bold.ttf"
bottomPerc = 15 # giving a 0 will place the title at the bottom & 100 at the top.
prefixText = "NFT"

# Input main photo to split
img = cv2.imread("nftRaw.png") 
img_shape = img.shape
tile_size = (720, 540)
offset = (720, 540)
path = "./Output/"
resizeFactor = 0.85
enableWhiteFiltering = False

# Frame management
def frameSelector(colorIndex):
    if (colorIndex == 0):
        myFrame = Image.open("frame1.png")
    else:
        myFrame = Image.open("frame2.png")    

    fW , fH = myFrame.size
    return myFrame, fW, fH

whiteCanvas = Image.new(mode = "RGB", size = tile_size, color = "#ffffff")
wW, wH = whiteCanvas.size

# Edit the keys and content of the json metadata according your needs.
def jsonGenerator(index, text, count):

    if( index == 0 ):
        frameColor = "Azure"
    else:
        frameColor = "Golden"
    
    json_file = {
  "description": "Your NFT description.", 
  "image": "https://rememberToEditThis", 
  "name": "NFT N° " + text,
  "attributes": [ 
          {
            "trait_type": "Frame Color", 
            "value": frameColor
        }
        ], 
    }
    with open("./Output/metadata/" + str(count) + ".json", "w+" ) as f:
        json_dump = json.dump(json_file, f)

# Slice main image and NFT Creation
nftCount = 0
for i in range(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
    for j in range(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
        cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]

        grayImage = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
        bwImg = cv2.bitwise_not(grayImage)
        
        if (cv2.countNonZero(bwImg) == 0 and enableWhiteFiltering == True):
            continue
        else:
            nftCount = 1 + nftCount
            print("Generating image: " + prefixText +" " + str(i) + "-" + str(j))
                        
            cv2_im_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)  
            pil_im = Image.fromarray(cv2_im_rgb) 
            w, h = pil_im.size
            draw = ImageDraw.Draw(pil_im)  

            font = ImageFont.truetype(font= fontRoute, size = fontSize)
            text = str("- " + str(i) + ":" + str(j) + " -")
            metadataText = str(str(i) + ":" + str(j))
            textsize = draw.textsize(text, font)

            textX = round((w - textsize[0]) / 2)
            textY = round(h - h * bottomPerc/100 )
            
            draw.text((textX, textY), text, font= font, fill=(0,0,0,255)) 

            # Paste Point Calculation (center align desired)
            newSize = (round(tile_size[0] * resizeFactor), round(tile_size[1] * resizeFactor))
            resizedImg = pil_im.resize(newSize)
            imW, imH = resizedImg.size
                
            ## PIL vs White Canvas
            xWP = round((abs(wW-imW))/2) # Paste position should be Canvas + xWP or yWP
            yWP = round((abs(wH-imH))/2)
            canvas = whiteCanvas.copy()
            canvas.paste(resizedImg, (xWP, yWP))

            # Image with canvas vs Frames. Yellow for even and blue for uneven.
            if( j % 2 == 0 ):
                index = 0
            else:
                index = 1
            
            frame, fW, fH = frameSelector(index)
            xIF = round((abs(fW-wW))/2)
            yIF = round((abs(fH-wH))/2)
            canvas = canvas.copy()
            canvas.paste(frame, (xIF, yIF), mask = frame)

            cv2_FinalImg = cv2.cvtColor(np.array(canvas), cv2.COLOR_RGB2BGR) 
            jsonGenerator(index, metadataText, nftCount)
            cv2.imwrite(os.path.join(path , str(nftCount) + ".png"), cv2_FinalImg)

imagesCreated = int(math.ceil(img_shape[0]/(offset[1] * 1.0))) * int(math.ceil(img_shape[1]/(offset[0] * 1.0)))

print("Process completed. Created " + str(imagesCreated) + " sliced images.")
