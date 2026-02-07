
from pathlib import Path
import utils

logger = utils.setup_logging()

def parse_structure(data):
    sections = []
    current = {"title":"Document","paragraphs":[]}
    pid = 0

    for page in data["pages"]:
        paragraphs = [p.strip() for p in page["text"].split("\n\n") if p.strip()]

        for p in paragraphs:
            para = {
                "id": f"para_{pid}",
                "text": p,
                "page": page["page_number"],
                "section": current["title"]
            }

            current["paragraphs"].append(para)
            pid += 1

    sections.append(current)

    return {
        "file_name": data["file_name"],
        "sections": sections
    }

def run(input_path: Path, output_path: Path):
    raw = utils.read_json(input_path)
    structured = parse_structure(raw)
    utils.write_json(structured, output_path)
    return output_path
