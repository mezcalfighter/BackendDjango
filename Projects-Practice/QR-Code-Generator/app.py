import qrcode

data = input("Enter text or URL: ")
name = input("Enter the file name: ")

img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save(f"{name}.png")