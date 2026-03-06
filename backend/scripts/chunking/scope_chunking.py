def chunk_scope_document(text, source_file, chunk_size=50, overlap=5):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = words[start:end]

        chunk_text = " ".join(chunk)

        metadata = {
            "source_file": source_file,
            "section": "unknown"
        }

        chunks.append({
            "text": chunk_text,
            "metadata": metadata
        })

        start += chunk_size - overlap

    return chunks