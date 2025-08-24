# utils/parser.py
import re
from typing import Dict

def parse_invoice(text: str) -> Dict[str, str]:
    lower_text = text.lower()

    # --- Тип документа ---
    if 'торг-12' in lower_text or 'накладная' in lower_text:
        doc_type = 'Товарная накладная'
    elif 'акт' in lower_text and 'фактура' not in lower_text:
        doc_type = 'Акт'
    else:
        doc_type = 'Счёт-фактура'

    # --- Дата ---
    date_match = re.search(r'\b(\d{2}[.\-/]\d{2}[.\-/]\d{4})\b', text)
    date = date_match.group(1) if date_match else 'Не найдено'

    # --- Номер ---
    num_match = re.search(r'[№#]\s*([A-ZА-Яa-zа-я0-9\-]+)', text)
    number = num_match.group(1) if num_match else 'Не найдено'

    # --- Поставщик ---
    supplier_match = re.search(r'поставщик[:\s]*"([^"]+)"', text, re.IGNORECASE)
    if supplier_match:
        supplier = supplier_match.group(1).strip()
    else:
        supplier_match = re.search(r'поставщик[:\s]*([А-Я][^,;\n]{5,})', text, re.IGNORECASE)
        supplier = supplier_match.group(1).strip() if supplier_match else 'Не найдено'

    # --- Итого: ищем "итого", потом любой текст, потом цифры ---
    total_match = re.search(r'итого.*?(\d[\d\s.,]+)', text, re.IGNORECASE)
    total = total_match.group(1).strip() if total_match else 'Не найдено'

    # --- НДС ---
    nds_match = re.search(r'ндс[^\d]*?([\d\s.,]+)', text, re.IGNORECASE)
    nds = nds_match.group(1).strip() if nds_match else 'Не найдено'

    return {
        "doc_type": doc_type,
        "date": date,
        "number": number,
        "supplier": supplier,
        "total": total,
        "nds": nds
    }
