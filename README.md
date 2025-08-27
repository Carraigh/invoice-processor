# Invoice Processor — Веб-интерфейс

Инструмент для автоматической обработки счетов-фактур, актов и накладных (PDF/сканы) → Excel.

Теперь с **веб-интерфейсом** — загрузи документ, получи данные и выгрузку в Excel.

![Web Interface Screenshot](screenshots/screenshot.png)

## Особенности
- Загрузка PDF и изображений через веб-форму
- OCR и парсинг данных (номер, дата, поставщик, сумма, НДС)
- Отображение результата на странице
- Скачивание Excel-файла
- Поддержка сканов и текстовых PDF

## Технологии
- Python, FastAPI (бэкенд)
- HTML/CSS/JS (фронтенд)
- OCR: pytesseract + OpenCV
- pandas, openpyxl
- Docker (опционально)

## Запуск

### 1. Создай виртуальное окружение

python -m venv venv
source venv/bin/activate

### 2. Установи зависимости

pip install -r requirements.txt

### 3. Запусти сервер

uvicorn web.main:app --reload

Открой: http://localhost:8000

### Через Docker

docker-compose up --build

