import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")
EMBEDDING_MODEL = "text-embedding-3-small"


def embed_texts(texts):
    """
    Generate embeddings for a list of texts
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    vectors = [item.embedding for item in response.data]

    return vectors


def prepare_for_embedding(chunk):
    """
    Convert chunk into embedding-friendly format
    """

    text = chunk["text"]
    metadata = chunk["metadata"]

    prefix = (
        f"Document Type: Scope Document | "
        f"File: {metadata['source_file']} | "
        f"Section: {metadata.get('section','unknown')} | "
    )

    return prefix + "\n" + text