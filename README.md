# invoice-processor

**Автоматизация обработки первичной бухгалтерской документации**
Скрипт для извлечения данных из **счетов-фактур, актов и накладных** (PDF/сканы) → в Excel.

## Зачем?
Бухгалтеры тратят часы на ручной ввод. Этот инструмент:
- Распознаёт текст (OCR)
- Находит ключевые поля
- Экспортирует в Excel
- Сокращает время обработки с 10 минут до 30 секунд

## Пример

**Ввод:**
PDF-скан счёта

**Вывод:**
| doc_type       | date       | number  | supplier       | total     | nds       |
|----------------|------------|---------|----------------|-----------|-----------|
| Счёт-фактура   | 15.04.2025 | СЧ-1024 | ООО "ТехноЛайн" | 118 000,00| 18 000,00 |

## Установка

# 1. Клонируй репозиторий
git clone https://github.com/Carraigh/invoice-processor.git
cd invoice-processor

# 2. Создай виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Установи зависимости
pip install -r requirements.txt

# 4. Установи системные утилиты (Debian/Ubuntu/Kali)
sudo apt install poppler-utils tesseract-ocr

# 5. Запусти
python main.py examples/sample.pdf

Технологии
Python, OCR (Tesseract)
pytesseract, pdf2image, Pillow, pandas
Регулярные выражения

Для кого?
Бухгалтеры
Финансовые аналитики
Аудиторы
FinOps
