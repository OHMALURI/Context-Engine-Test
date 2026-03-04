import os
import sys

# Fix path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from scripts.parsing.transcript_parser import parse_transcript
from scripts.vector_store.chunking import chunk_transcript
from scripts.vector_store.embeddings import embed_texts, prepare_for_embedding
from scripts.vector_store.milvus_client import get_collection


# -----------------------------
# CONFIG
# -----------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
DATA_FOLDER = os.path.join(BASE_DIR, "Data", "Transcripts")

DEBUG_PREVIEW = True          # Print sample chunks
PREVIEW_LIMIT = 3             # How many chunks to show


def load_transcript_files(folder_path: str):
    """Return all .md transcript file paths"""
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".md")
    ]


def main():
    print("🔹 Starting Transcript Ingestion Pipeline...\n")

    transcript_files = load_transcript_files(DATA_FOLDER)

    if not transcript_files:
        print("❌ No transcripts found in Data folder.")
        return

    print(f"Found {len(transcript_files)} transcript files\n")

    all_prepared_chunks = []

    # -----------------------------
    # Parse + Chunk
    # -----------------------------
    for file_path in transcript_files:
        print(f"Processing: {os.path.basename(file_path)}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        transcript = parse_transcript(content)
        chunks = chunk_transcript(transcript)

        print(f"  → Created {len(chunks)} chunks")

        for chunk in chunks:
            prepared_text = prepare_for_embedding(chunk)
            all_prepared_chunks.append(prepared_text)

    print(f"\nTotal chunks created: {len(all_prepared_chunks)}")

    # -----------------------------
    # DEBUG PREVIEW (TEXT OUTPUT)
    # -----------------------------
    if DEBUG_PREVIEW:
        print("\n🔍 Previewing Sample Chunks:\n")
        for i, text in enumerate(all_prepared_chunks[:PREVIEW_LIMIT]):
            print(f"\n--- Chunk {i+1} ---")
            print(text)
            print("-" * 80)

    # -----------------------------
    # Generate Embeddings
    # -----------------------------
    print("\n🔹 Generating embeddings (OpenAI)...")
    vectors = embed_texts(all_prepared_chunks)

    print(f"Generated {len(vectors)} embeddings")

    # Show embedding dimension
    if vectors:
        print(f"Embedding dimension: {len(vectors[0])}")

    # -----------------------------
    # Store in Milvus
    # -----------------------------
    print("\n🔹 Connecting to Milvus...")
    collection = get_collection()

    print("Inserting into Milvus...")
    collection.insert([vectors, all_prepared_chunks])
    collection.flush()

    print("\n✅ INGESTION COMPLETE")
    print(f"Inserted {len(vectors)} records into Milvus.\n")


if __name__ == "__main__":
    main()