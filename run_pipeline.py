
from pathlib import Path
import ingest
import structure
import semantic
import build_kg

def run_pipeline(pdf_path):
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    raw = ingest.run(pdf_path, output_dir/"raw.json")
    structured = structure.run(raw, output_dir/"structured.json")
    entities = semantic.run(structured, output_dir/"entities.json")
    build_kg.run(structured, entities, output_dir/"kg.graphml")

if __name__ == "__main__":
    import sys
    run_pipeline(Path(sys.argv[1]))
