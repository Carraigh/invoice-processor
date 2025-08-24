# main.py
from utils.ocr import extract_text_from_pdf
from utils.parser import parse_invoice
from utils.exporter import save_to_excel
import sys

def main(pdf_path: str, output_path: str = "output/invoices.xlsx"):
    print(f"📄 Обработка документа: {pdf_path}")
    
    # 1. Извлекаем текст
    text = extract_text_from_pdf(pdf_path)
    
    # 2. Парсим данные
    data = parse_invoice(text)
    
    # 3. Сохраняем в Excel
    save_to_excel([data], output_path)
    
    # 4. Выводим результат
    print(f"✅ Готово! Результат: {output_path}")
    print(f"📊 Извлечено: {data}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("❗ Укажите путь к PDF: python main.py examples/sample.pdf")
