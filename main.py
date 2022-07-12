
from PIL import Image
import os

downloadsFolder = "C:\\Users\\JDARD\\Downloads\\"
picturesFolder = "C:\\Users\\JDARD\\OneDrive\\Imágenes\\Saved Pictures\\"

#crear Main
if __name__ == "__main__":
    #recorrer carpeta de downloadsFolder
    for filename in os.listdir(downloadsFolder):
        name, ext = os.path.splitext(downloadsFolder + filename)
        if ext in [".jpg", ".jpeg", ".png"]:
            #abrir imagen
            im = Image.open(downloadsFolder + filename)
            #comprimir imagen y guardar
            im.save(picturesFolder + "_Compresed" + filename,optimize = True, quality=60)
            print("Imagen comprimida")