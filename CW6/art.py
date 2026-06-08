from PIL import Image, ImageFilter

with Image.open("in.jpeg") as img:
    print(img.size)
    print(img.format)
    img = img.rotate(180)
    img = img.filter(ImageFilter.BLUR)
    img.save("art.jpeg")
