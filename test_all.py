# test_all.py
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import pandas as pd

print("✅ Все библиотеки импортированы!")

# Проверка Tesseract
print("🔧 Версия Tesseract:", pytesseract.get_tesseract_version())

# Попробуем создать изображение
img = Image.new('RGB', (50, 50), 'blue')
img.save('test_blue.png')
print("🎨 Изображение создано: test_blue.png")

