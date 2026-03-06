import os

# Transcript pipeline
from scripts.parsing.transcript_parser import parse_transcript
from scripts.chunking.transcript_chunking import chunk_transcript
from scripts.embedding.transcript_embedding import embed_texts

# Scope pipeline
from scripts.parsing.scope_parser import parse_scope_document
from scripts.chunking.scope_chunking import chunk_scope_document
from scripts.embedding.scope_embedding import embed_scope_texts

# Milvus
from scripts.vector_store.milvus_client import get_collection


TRANSCRIPT_PATH = "Data/Transcripts"
SCOPE_PATH = "Data/ScopeDocs"


# ------------------------------------------------
# TRANSCRIPT DEBUG
# ------------------------------------------------

def debug_transcripts():

    print("\n==============================")
    print("🔎 DEBUGGING TRANSCRIPT PIPELINE")
    print("==============================\n")

    files = [f for f in os.listdir(TRANSCRIPT_PATH) if f.endswith(".md")]

    if len(files) == 0:
        print("❌ No transcript files found")
        return

    file = files[0]
    path = os.path.join(TRANSCRIPT_PATH, file)

    print(f"📄 Testing file: {file}")

    # PARSING
    text = parse_transcript(path)

    print("✅ Parsing successful")
    print("Text length:", len(text))

    # CHUNKING
    chunks = chunk_transcript(text)

    print("✅ Chunking successful")
    print("Chunks created:", len(chunks))

    print("\nSample Chunk:\n")
    print(chunks[0][:200])

    # EMBEDDINGS
    embeddings = embed_texts(chunks[:3])

    print("\n✅ Embeddings generated")
    print("Embedding size:", len(embeddings[0]))

    # MILVUS
    collection = get_collection("transcript_debug")

    collection.insert([embeddings, chunks[:3]])
    collection.flush()

    print("✅ Inserted into Milvus")


# ------------------------------------------------
# SCOPE DOC DEBUG
# ------------------------------------------------

def debug_scope_docs():

    print("\n==============================")
    print("🔎 DEBUGGING SCOPE DOC PIPELINE")
    print("==============================\n")

    files = os.listdir(SCOPE_PATH)

    if len(files) == 0:
        print("❌ No scope docs found")
        return

    file = files[0]
    path = os.path.join(SCOPE_PATH, file)

    print(f"📄 Testing file: {file}")

    # PARSING
    text = parse_scope_document(path)

    print("✅ Parsing successful")
    print("Text length:", len(text))

    # CHUNKING
    chunks = chunk_scope_document(text)

    print("✅ Chunking successful")
    print("Chunks created:", len(chunks))

    print("\nSample Chunk:\n")
    print(chunks[0][:200])

    # EMBEDDINGS
    embeddings = embed_scope_texts(chunks[:3])

    print("\n✅ Embeddings generated")
    print("Embedding size:", len(embeddings[0]))

    # MILVUS
    collection = get_collection("scope_debug")

    collection.insert([embeddings, chunks[:3]])
    collection.flush()

    print("✅ Inserted into Milvus")


# ------------------------------------------------
# MAIN DEBUG RUNNER
# ------------------------------------------------

def main():

    print("\n🚀 RUNNING FULL INGESTION DEBUG\n")

    debug_transcripts()

    debug_scope_docs()

    print("\n🎉 ALL PIPELINES TESTED\n")


if __name__ == "__main__":
    main()