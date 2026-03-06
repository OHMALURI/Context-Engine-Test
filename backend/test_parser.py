import os
from scripts.parsing.transcript_parser import parse_transcript
from scripts.vector_store.chunking import chunk_transcript


# 1️⃣ Load transcript file
filepath = os.path.join("..", "data", "transcripts", "Capstone-Bee-Hive-Onboarding-9e0a808f-6eb5.md")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 2️⃣ Parse transcript
transcript = parse_transcript(content)

print("Project:", transcript.project)
print("Meeting Type:", transcript.meeting_type)
print("Date:", transcript.date)
print("Start Time:", transcript.start_time)
print("Number of turns:", len(transcript.turns))

# 3️⃣ Chunk transcript
chunks = chunk_transcript(transcript, window=6, overlap=2)

print("\nNumber of chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0]["text"])
print("\nMetadata:\n", chunks[0]["metadata"])


from backend.scripts.embedding.transcript_embedding import prepare_for_embedding, embed_texts

texts = [prepare_for_embedding(chunk) for chunk in chunks]

vectors = embed_texts(texts)

print("Embedding dimension:", len(vectors[0]))