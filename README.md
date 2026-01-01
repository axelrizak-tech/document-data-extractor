# document-data-extractor

## Business problem

Companies receive large volumes of documents every day:
- invoices in PDF format,
- text reports,
- CSV exports,
- Excel files from various systems.
These files often differ in structure and require manual review, which is:
- time-consuming,
- error-prone,
- not scalable.
This project demonstrates how such documents can be automatically processed and analyzed using Python.

## What this solution does

The script automatically:
- accepts uploaded files (PDF, TXT, CSV, XLSX),
- detects the file type,
- extracts text or tabular data,
- applies simple business logic to identify key information,
- generates structured output files for further processing.

## Example logic implemented

For PDF / TXT files:
- scans text line by line,
- detects lines containing keywords such as INVOICE, TOTAL.

For CSV / XLSX files:
- loads the table,
- outputs:
number of rows,
column names.
This logic is intentionally simple and transparent, designed as a base for more advanced rules.

## Output examples

Depending on file type, the script produces:
- extracted key text lines (PDF / TXT),
- summary files for tables (CSV / XLSX),
- clear logging messages for each processed file,
- graceful error handling for invalid or corrupted files.

## Error handling

Invalid PDFs are safely skipped with an informative message.
Unsupported file types are ignored.
Processing continues even if one file fails.
This makes the solution suitable for batch processing.
