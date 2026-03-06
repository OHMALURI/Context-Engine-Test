from typing import List, Dict
from scripts.parsing.transcript_parser import Transcript


def chunk_transcript(
    transcript: Transcript,
    window: int = 6,
    overlap: int = 2
) -> List[Dict]:

    turns = transcript.turns
    chunks = []

    step = window - overlap

    for i in range(0, len(turns), step):
        window_turns = turns[i:i + window]

        if not window_turns:
            continue

        # Combine text
        combined_text = "\n".join(
            f"{t.speaker} [{t.timestamp}]: {t.text}"
            for t in window_turns
        )

        metadata = {
            "project": transcript.project,
            "meeting_type": transcript.meeting_type,
            "date": transcript.date,
            "speakers": list({t.speaker for t in window_turns}),
            "start_time": window_turns[0].timestamp,
            "end_time": window_turns[-1].timestamp
        }

        chunks.append({
            "text": combined_text,
            "metadata": metadata
        })

    return chunks