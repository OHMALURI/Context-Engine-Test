import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scripts.parsing.scope_parser import parse_scope_document
from scripts.chunking.scope_chunking import chunk_scope_document
from scripts.embedding.scope_embedding import embed_texts, prepare_for_embedding
from scripts.vector_store.milvus_client import get_collection


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

DATA_FOLDER = os.path.join(BASE_DIR, "Data", "ScopeDocs")

DEBUG_PREVIEW = True          # Print sample chunks
PREVIEW_LIMIT = 3             # How many chunks to show


def load_scope_files(folder_path):

    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith((".pdf", ".docx", ".pptx"))
    ]


def main():

    print("Starting Scope Document Ingestion\n")

    files = load_scope_files(DATA_FOLDER)

    if not files:
        print("No scope documents found")
        return

    print(f"Found {len(files)} scope documents\n")

    all_chunks = []

    for file_path in files:

        print(f"Processing: {os.path.basename(file_path)}")

        text = parse_scope_document(file_path)

        if not text:
            continue

        chunks = chunk_scope_document(text, os.path.basename(file_path))

        print(f"Created {len(chunks)} chunks")

        all_chunks.extend(chunks)

    print(f"\nTotal chunks: {len(all_chunks)}")

    print("\nGenerating embeddings...")

    prepared_texts = [prepare_for_embedding(chunk) for chunk in all_chunks]

    # -----------------------------
    # DEBUG PREVIEW (TEXT OUTPUT)
    # -----------------------------
    if DEBUG_PREVIEW:
        print("\n🔍 Previewing Sample Chunks:\n")
        for i, text in enumerate(prepared_texts[:PREVIEW_LIMIT]):
            print(f"\n--- Chunk {i+1} ---")
            print(text)
            print("-" * 80)

    vectors = embed_texts(prepared_texts)

    print(f"Generated {len(vectors)} embeddings")

    print("\nConnecting to Milvus...")

    collection = get_collection("scope_embeddings")

    print("Inserting into Milvus...")

    collection.insert([vectors, prepared_texts])

    collection.flush()

    print("\nScope ingestion complete")

    print(f"Inserted {len(vectors)} records into Milvus")


if __name__ == "__main__":
    main()