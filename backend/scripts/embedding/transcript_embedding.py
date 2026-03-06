import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")

EMBEDDING_MODEL = "text-embedding-3-small"

# Prepares text with metadata
def prepare_for_embedding(chunk: dict) -> str:
    m = chunk["metadata"]
    prefix = (
        f"Project: {m['project']} | "
        f"Meeting: {m['meeting_type']} | "
        f"Date: {m['date']} | "
        f"Speakers: {', '.join(m['speakers'])}\n\n"
    )
    return prefix + chunk["text"]

# Generates embeddings for a list of text chunks
def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]