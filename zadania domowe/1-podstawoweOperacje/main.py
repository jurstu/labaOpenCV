import requests
from cv2 import imshow
import numpy as np
from PIL import Image
from io import BytesIO 
import matplotlib.pyplot as plt



url = 'https://i.insider.com/602ee9ced3ad27001837f2ac?width=700'
response = requests.get(url, stream=True)
img = Image.open(BytesIO(response.content))
img.save("orig.png")


img = np.array(img)

red = img.copy()
red[:,:,1] = 0
red[:,:,2] = 0

imshow("obraz", img)

green = img.copy()
green[:,:,0] = 0
green[:,:,2] = 0

blue = img.copy()
blue[:,:,1] = 0
blue[:,:,0] = 0



red = Image.fromarray(red)
red.save("red.png")

green = Image.fromarray(green)
green.save("green.png")

blue = Image.fromarray(blue)
blue.save("blue.png")



print("shape is", img.shape, "data type is", img.dtype)
print("theoretical size of the image in memory: 1Byte/color * 3colors/pixel * width * height = ")
print("= 1 * 3 * 525 * 700 = ", 1 * 3 * img.shape[0] * img.shape[1], "Bytes, that is: {: 2.2f}".format(1 * 3 * img.shape[0] * img.shape[1]/1024), "kB")

print("Memory size of img object in bytes: ", img.size)
print("this image is stored on", img.device)