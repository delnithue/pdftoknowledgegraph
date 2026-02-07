# PDF to Knowledge Graph Pipeline

This project converts a PDF document into a structured Knowledge Graph using a modular Python pipeline.

## Problem Overview
The goal is to:
- Extract text from a PDF
- Identify document structure (sections and paragraphs)
- Extract semantic entities
- Build a Knowledge Graph representing the document

## Project Structure
pdf_to_kg/
├── ingest.py # PDF text extraction
├── structure.py # Section & paragraph parsing
├── semantic.py # Named entity extraction
├── build_kg.py # Knowledge graph construction
├── run_pipeline.py # Pipeline orchestration
├── utils.py # Shared utilities
├── requirements.txt # Dependencies


## Pipeline Stages

1. **Ingestion**
   - Extracts text and metadata from the PDF

2. **Structure Parsing**
   - Splits document into sections and paragraphs

3. **Semantic Extraction**
   - Extracts named entities using spaCy

4. **Knowledge Graph Construction**
   - Builds nodes and edges using NetworkX

## How to Run

### Install dependencies 


### Run the pipeline


## Output
- `raw_text.json` – extracted PDF text
- `structured.json` – parsed sections and paragraphs
- `entities.json` – extracted entities
- `kg.graphml` – knowledge graph file

## Tools Used
- pdfplumber
- spaCy
- NetworkX

## Notes
This project is designed to be modular, interpretable, and easy to extend with LLM-based extraction or graph databases.
