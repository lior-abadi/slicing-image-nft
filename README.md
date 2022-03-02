# slicing-image-nft
## Main purpose of each program
### nftGeneration.py
- This program takes an image as an input and generates slices of the desired size. 
- To each slice it assigns a frame and overlays with a text generated in a coordinate way. 
- Also, it filters and discards all the slices that are completely white. +
- When each slice is created with the proper frame and coordinates, it saves the file to the Output folder and generates the metadata (following Opensea standards) for each slice.



## Instructions
1) Get an big image (Adobe Illustrator or another SVG creator is recommended. Export for screens at 30x for bigger images).
2) Calculate the size of the slices respecting the relationship of aspect (1:1, 3:2, among others), simply calculate width/height.
3) Inputs to be set:
   - fontSize
   - bottomPerc (margin from the bottom of the overlay text)
   - prefixText 
   - imread Route (edit with the route pointing to the main big image to be sliced.
   - tile_size (edit with the desired slice size)
   - offset (to transform all the image to tiles, set the same as tile_size. If other value is provided more or less slices will be generated with/without overlap)
   - resizeFactor (to keep aspect ratio with the frames) 
