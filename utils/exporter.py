# utils/exporter.py
import pandas as pd
import json
import os

def save_to_excel(data_list, output_path: str):
    """
    Сохраняет данные в Excel и дополнительно экспортирует в JSON для веб-интерфейса.
    
    :param data_list: Список словарей с данными (например, [invoice_data])
    :param output_path: Путь к файлу Excel (например, "output/invoices.xlsx")
    """
    # Преобразуем в DataFrame и сохраняем в Excel
    df = pd.DataFrame(data_list)
    df.to_excel(output_path, index=False)
    
    # Сохраняем JSON-версию для веб-интерфейса
    json_path = output_path.replace(".xlsx", ".json")
    os.makedirs(os.path.dirname(json_path) if os.path.dirname(json_path) else ".", exist_ok=True)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

    print(f"📊 Данные сохранены: {output_path} и {json_path}")
