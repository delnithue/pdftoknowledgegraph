
import spacy
from pathlib import Path
import utils

logger = utils.setup_logging()
nlp = spacy.load("en_core_web_sm")

def extract_entities(data):
    results = []

    for section in data["sections"]:
        for paragraph in section["paragraphs"]:
            doc = nlp(paragraph["text"])

            for ent in doc.ents:
                results.append({
                    "text": ent.text,
                    "type": ent.label_,
                    "paragraph_id": paragraph["id"],
                    "page": paragraph["page"]
                })

    return {
        "file_name": data["file_name"],
        "entities": results
    }

def run(input_path: Path, output_path: Path):
    structured = utils.read_json(input_path)
    entities = extract_entities(structured)
    utils.write_json(entities, output_path)
    return output_path
