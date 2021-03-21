from PIL import Image

ashok_image = Image.open('ashok.jpg')

print(ashok_image.format)
print(ashok_image.size)

rotate_image = ashok_image.rotate(45)
rotate_image.show()