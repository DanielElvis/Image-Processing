import pytesseract
from PIL import Image

# Tesseract Config
pytesseract.pytesseract.tesseract_cmd = r"path/to/tesseract.exe"


# example

def image_to_string(img):
    image = Image.open(img)
    response = pytesseract.image_to_string(image)
    return f" Your Text Is : {response}"

print(image_to_string("your image *"))

