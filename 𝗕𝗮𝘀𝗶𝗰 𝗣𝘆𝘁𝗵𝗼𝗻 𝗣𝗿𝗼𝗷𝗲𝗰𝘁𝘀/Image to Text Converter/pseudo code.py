
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = input("Enter image path here: ").strip().strip('"')

image = Image.open(img)

text = pytesseract.image_to_string(image)

print(text)


#its working now we will build a streamlit application around it 
