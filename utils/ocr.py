import pytesseract
from PIL import Image

def extract_text(img_path):
    img = Image.open(img_path)
    return pytesseract.image_to_string(img)
