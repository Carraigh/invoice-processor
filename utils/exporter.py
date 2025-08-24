# utils/exporter.py
import pandas as pd

def save_to_excel(data, output_path: str):
    """Сохраняет данные в Excel"""
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
