from PIL import Image

im = Image.open("poto.jpg")

print(im.format)
print(im.mode)
print(str(im.size))

im.show()