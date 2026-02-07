
import pdfplumber
from pathlib import Path
import utils

logger = utils.setup_logging()

def extract_pdf(pdf_path: Path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = []

        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ""
            pages.append({
                "page_number": page_num,
                "text": text
            })

        return {
            "file_name": pdf_path.name,
            "total_pages": len(pdf.pages),
            "pages": pages
        }

def run(pdf_path: Path, output_path: Path):
    data = extract_pdf(pdf_path)
    utils.write_json(data, output_path)
    return output_path
