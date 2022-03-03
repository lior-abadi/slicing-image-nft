# slicing-image-nft
## Program Overviews
This program can be used for several purposes. It has a modular design and fully adaptable code which gives flexibility to the user. If used end to end with the instructions provided below, a full NFT collection with proper Metadata (and each image CID link) will be generated. You can use just parts of it to achieve your needs. The slicing image process can be done with Photoshop (e.g.) but will need a powerful machine to do so.  With this code the same output is achieved with less performance needed.
Enjoy!

### nftGeneration.py
- This program takes a big image as an input and generates slices of the desired size. 
- For each slice it assigns a frame and overlays it with a text generated in a coordinate way. 
- Also, it filters and discards all the slices that are completely white. 
- When each slice is created with the proper frame and coordinates, it saves the file to the Output folder and generates the metadata (following Opensea standards) for each slice.

### nftMetadataEdit.py
- Once you upload all your sliced images folder to the IPFS service of your choice (e.g. Pinata), the system gives a CID to that folder followed by /nftName.json which needs to be replaced on each metadata file. 
- This file takes an imput of the image folder CID and modifies each .json file.

### nftCoordinateGenerator.py
- Takes the main big image, vertical and horizontal lines made in Illustrator (or other SVG creator) and adds them to the main big image creating a grid.
- The horizontal and vertical lines should have the width or height of the big image. For example, for a 24,000x18,000 image the vertical lines should have 18,000px of height and the horizontal 24,000px of width.
- Load each content as well as keeping the offset ratio given into the **nftGeneration.py** program.

### nftAddCoordinateNumber.py
- Loads the image with vertical and horizontal coordinate lines and adds the respective coordinates for each row and column (that will be corresponded with the indexes overlayed on each sliced image created before using **nftGeneration.py**


## Instructions (in running order)
To run each program just go to the directory where it is stored and:
```
python (program_name)
```
For example:
```
python nftGeneration.py
```

### nftGeneration.py
1) Get an big image (Adobe Illustrator or another SVG creator is recommended. Export for screens at 30x for bigger images).
2) Calculate the size of the slices respecting the relationship of aspect (1:1, 3:2, among others), simply calculate width/height.
3) The frame and the image should have the same size (also this will be the final slice size). The program itself adjust the overlapping with the resizeFactor.
4) Inputs to be set:
```
   - fontSize
   - fontRoute (the route to the .ttf font)
   - bottomPerc (margin from the bottom of the overlay text)
   - prefixText 
   - imread Route (edit with the route pointing to the main big image to be sliced.
   - tile_size (edit with the desired slice size)
   - offset (to transform all the image to tiles, set the same as tile_size. If other value is provided more or less slices will be generated with/without overlap)
   - resizeFactor (to keep aspect ratio with the frames) 
   - myFrame route to each designed frame (you can edit the if statement to have all the desired indexes depending the amount of frames.
   - frameColor (the same as mFrame but with their names).
   - jsonGenerator (edit the json file to one that matches your needs).
```
5) Run.


### nftMetadataEdit.py
1) Upload all the images folder generated by the last program to Pinata (for example). It is important to upload the folder itself
2) Copy the CID of the folder and make sure that each NFT image is pointed as: ipfs://CID/nftName.json where each "nftName" would be its number.
3) Replace the CID link of the folder on:
```
imageCIDs = "ipfs://_CID_/"
```
4) Run.


### nftCoordinateGenerator.py
1) Create the vertical and horizontal line following the instructions made on the **Program Overview** section.
2) Set the **offset** the same as the **nftGeneration.py** program.
3) Make sure that the loaded image under the line 9 is the same as the sliced image from before.
4) Load the vertical an horizontal lines created in lines 18 and 19.
5) Run.


### nftAddCoordinateNumber.py
1) Make sure that the input path of the image is the one with the horizontal and vertical lines (in line 9)
2) Select a fontSize and fontType
3) Under each generator (vertical and horizontal) there are **adjustmentFactors** that will help you match each number with the available space between rows and columns
4) You can add and tweak the **if statement** within each generator to adjust a specific number acording your needs as well as each **adjustmentFactor**.
5) Run.
