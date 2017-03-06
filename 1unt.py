from Tkinter import Tk
from PIL import Image, ImageFilter, ImageOps
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

img = Image.open(filename)
img.show()

img2 = img.crop((0,0,100,100))
img2.show()
sys.exit()
img2.save("/Users/marcoaguilera/Desktop/Python/2bn.png")

sys.exit()
def filterTest(filename):
    image = Image.open(filename)
    image.mode
    imageFT = image.convert("L")
    imageFT.show()
    imageFt.save("/Users/marcoaguilera/Desktop/Python/1bn.png")

filterTest(filename)

sys.exit("TEST")
imagen = Image.open("1.png")
imagen.mode
imagenbn = imagen.convert("L")
imagenbn.show()
imagenbn.save("1bn.png")

imagen = Image.open("1.png")
unfocused = imagen.filter(ImageFilter.BLUR)
unfocused.show()
unfocused.save("unfocused.png")

imagen = Image.open("1.png")
imagen2 = imagen.filter(ImageFilter.MinFilter(3))
imagen2.show()
imagen2.save("min3.png")

imagen = Image.open("1.png")
sharp = imagen.filter(ImageFilter.SHARPEN)
sharp.show()
sharp.save("sharp.png")

imagen = Image.open("1.png")
imagen.mode
imagen3 = imagen.convert("P")
imagen3.show()
imagen3.save("min.png")

imagen = Image.open("1.png")
emb = imagen.filter(ImageFilter.EMBOSS)
emb.show()
emb.save("emb.png")

imagen = Image.open("1.png")
cont = imagen.filter(ImageFilter.CONTOUR)
cont.show()
cont.save("cont.png")

image = Image.open("1.png")
invert = ImageOps.invert(image)
invert.show()
invert.save("invert.png")

image = Image.open("1.png")
sol = ImageOps.solarize(imagen, threshold=65)
sol.show()
sol.save("sol.png")

image = Image.open("1.png")
aCont = ImageOps.autocontrast(imagen, cutoff=0)
aCont.show()
aCont.save("auto.png")
