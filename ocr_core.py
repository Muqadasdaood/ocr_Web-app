# ocr_core.py
import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en', 'ur'])

def extract_text(img):
    img_np = np.array(img)
    result = reader.readtext(img_np, detail=0)
    return "\n".join(result)