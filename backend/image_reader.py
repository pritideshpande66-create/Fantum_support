from PIL import Image
import pytesseract

def read_image(path):
    image = Image.open(path)
    return pytesseract.image_to_string(image)
