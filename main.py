!pip install pdfplumber pandas openpyxl matplotlib

import os
import pandas as pd
import pdfplumber
from google.colab import files

# KROK 1 — WGRANIE PLIKÓW

uploaded = files.upload()

# folder na wyniki
os.makedirs("results", exist_ok=True)

# LOGGING

def log(msg):
    print(f"[INFO] {msg}")

def log_error(msg):
    print(f"[ERROR] {msg}")

# PDF

def extract_text_from_pdf(path):
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise ValueError(f"To nie jest poprawny PDF: {e}")
    return text.strip()

# TXT

def extract_text_from_txt(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"Błąd odczytu TXT: {e}")

# CSV / XLSX

def load_table(path):
    try:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        elif path.endswith(".xlsx"):
            return pd.read_excel(path)
    except Exception as e:
        raise ValueError(f"Błąd odczytu tabeli: {e}")

# PROSTA LOGIKA BIZNESOWA

def analyze_text(text):
    result = {
        "invoice_line": None,
        "total_line": None
    }

    for line in text.splitlines():
        if "INVOICE" in line.upper():
            result["invoice_line"] = line.strip()
        if "TOTAL" in line.upper():
            result["total_line"] = line.strip()

    return result

# PROCESSOR JEDNEGO PLIKU

def process_file(file_path):
    file_name = os.path.basename(file_path)
    log(f"Przetwarzam plik: {file_name}")

    try:
        if file_name.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
            result = analyze_text(text)

            output_path = f"results/{file_name}_result.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(str(result))

            log("PDF przetworzony poprawnie")

        elif file_name.lower().endswith(".txt"):
            text = extract_text_from_txt(file_path)
            result = analyze_text(text)

            output_path = f"results/{file_name}_result.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(str(result))

            log("TXT przetworzony poprawnie")

        elif file_name.lower().endswith((".csv", ".xlsx")):
            df = load_table(file_path)

            output_path = f"results/{file_name}_summary.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"Liczba wierszy: {df.shape[0]}\n")
                f.write(f"Kolumny: {list(df.columns)}\n")

            log("Plik tabelaryczny przetworzony poprawnie")

        else:
            log_error("Nieobsługiwany typ pliku")

    except ValueError as e:
        log_error(str(e))
        log("Plik pominięty — przechodzę dalej")

# RUN

for file_name in uploaded.keys():
    process_file(file_name)
    print("-" * 50)

log("Wszystkie pliki przetworzone")
