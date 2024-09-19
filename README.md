# Image-Processing
This is an image processing project that can extract the text inside your images

<br>
<br>

> [!IMPORTANT]  
You must download the tesseract library as follows:<br>

```powershell
pip install pytesseract
```

<br>
<br>

> [!NOTE]
> To run this project, you must download the tesseract software and connect tesseract.exe to your project from within it, as in the following example:
>
> ```python
> pytesseract.pytesseract.tesseract_cmd = r"path/to/tesseract.exe"
> ```
>
> # Example
>
> ```python
> import pytesseract
from PIL import Image

# Tesseract Config
pytesseract.pytesseract.tesseract_cmd = r"path/to/tesseract.exe"


# example

def image_to_string(img):
    image = Image.open(img)
    response = pytesseract.image_to_string(image)
    return f" Your Text Is : {response}"

print(image_to_string("your image *"))

> ```

# Download Tesseract.exe with :
<p>https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe</p>


