
import networkx as nx
from pathlib import Path
import utils

logger = utils.setup_logging()

def build_graph(structured, entities):
    G = nx.Graph()

    doc_id = "doc"
    G.add_node(doc_id, type="document", name=structured["file_name"])

    for sid, section in enumerate(structured["sections"]):
        sec_id = f"section_{sid}"
        G.add_node(sec_id, type="section", title=section["title"])
        G.add_edge(doc_id, sec_id, type="HAS_SECTION")

        for para in section["paragraphs"]:
            pid = para["id"]
            G.add_node(pid, type="paragraph", page=para["page"])
            G.add_edge(sec_id, pid, type="HAS_PARAGRAPH")

    for eid, entity in enumerate(entities["entities"]):
        node_id = f"entity_{eid}"
        G.add_node(node_id, type="entity", text=entity["text"])
        G.add_edge(entity["paragraph_id"], node_id, type="MENTIONS")

    return G

def run(structured_path: Path, entity_path: Path, output_path: Path):
    structured = utils.read_json(structured_path)
    entities = utils.read_json(entity_path)

    G = build_graph(structured, entities)

    nx.write_graphml(G, output_path)
    return output_path
