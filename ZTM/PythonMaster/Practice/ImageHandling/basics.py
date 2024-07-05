from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
print(img.format) # It returns JPEG
print(img.size) # (640,640) 
print(img.mode) #RGB
print(dir(img)) # Prints all methods

# Adds filter to the image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png","png")

# Converts Image
converted_img = img.convert("L")
converted_img.save("grey.png","png")

#Show Image
img.show()

# Rotate
crooked = img.rotate(90)
crooked.save("crooked.png","png")

#Resize
resize = img.resize((300,300))
resize.save("resized.png","png")

# Crop 
box = (100,100,400,400)
region = img.crop(box)
region.save("croppped.png","png")

# Make it smaller size
astro = Image.open("./astro.jpg")
print(astro.size) # We need to know the size of the image
new_astro = astro.resize((400,400))
astro.save("thumbnail.jpg")

astro.thumbnail((400,400))
astro.save("new_thumbnail.jpg")

