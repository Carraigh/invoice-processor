from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import subprocess
import json

app = FastAPI()

# Подключаем шаблоны и статику
templates = Jinja2Templates(directory="web/templates")
app.mount("/static", StaticFiles(directory="web/static"), name="static")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/upload")
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    # Проверяем тип файла
    if not file.filename.lower().endswith((".pdf", ".jpg", ".jpeg", ".png")):
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Поддерживаются только PDF и изображения"
        })

    # Пути
    input_path = f"temp/{file.filename}"
    output_path = "temp/result.xlsx"

    # Создаём папку temp
    os.makedirs("temp", exist_ok=True)

    # Сохраняем загруженный файл
    with open(input_path, "wb") as f:
        f.write(await file.read())

    try:
        # Запускаем main.py
        subprocess.run(["python", "main.py", input_path, output_path], check=True)

        # Читаем результат (предположим, что save_to_excel возвращает JSON или мы его логируем)
        result_json = output_path.replace(".xlsx", ".json")
        result_data = {}
        if os.path.exists(result_json):
            with open(result_json, "r", encoding="utf-8") as f:
                result_data = json.load(f)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": result_data,
            "excel_file": "result.xlsx",
            "filename": file.filename
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Ошибка обработки: {str(e)}"
        })

@app.get("/download/{filename}")
async def download_file(filename: str):
    return FileResponse(f"temp/{filename}", filename=filename, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
