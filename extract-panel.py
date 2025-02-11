import pymupdf
import os
from image_processing.panel import extract_panels_custom

images_dir = "extracted-images"
panels_dir = "extracted-panels"

# Create the output directory if it doesn't exist
os.makedirs(images_dir, exist_ok=True)
os.makedirs(panels_dir, exist_ok=True)

doc = pymupdf.open("test.pdf") # open a document

for page_index in range(len(doc)): # iterate over pdf pages
    page = doc[page_index] # get the page
    image_list = page.get_images()

    # print the number of images found on the page
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index+1}")
    else:
        print("No images found on page", page_index+1)

    for image_index, img in enumerate(image_list, start=1): # enumerate the image list
        xref = img[0] # get the XREF of the image
        pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

        if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        
        output_path = os.path.join("extracted-images", f"{page_index+1}_{image_index+1}.png")

        pix.save(output_path) # save the image as png
        pix = None
    
# Extract panels from the saved image
extract_panels_custom(images_dir, panels_dir)