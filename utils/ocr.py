# utils/ocr.py
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path: str) -> str:
    """Конвертирует PDF в изображения с высоким DPI и извлекает текст через OCR"""
    images = convert_from_path(
        pdf_path,
        dpi=300,               # Высокое разрешение для лучшего OCR
        poppler_path='/usr/bin' # Работает на Linux
    )
    full_text = ""
    for i, image in enumerate(images):
        # Указываем язык: русский + английский
        text = pytesseract.image_to_string(image, lang='rus+eng')
        full_text += f"\n--- Страница {i+1} ---\n{text}\n"
    return full_text
