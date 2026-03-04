import re
from dataclasses import dataclass
from typing import List


# -----------------------------
# Data Structures
# -----------------------------

@dataclass
class Turn:
    speaker: str
    timestamp: str
    text: str


@dataclass
class Transcript:
    capstone: str
    project: str
    meeting_type: str
    date: str
    start_time: str
    turns: List[Turn]


# -----------------------------
# Parser Function
# -----------------------------

def parse_transcript(content: str) -> Transcript:
    lines = content.strip().split("\n")

    # -----------------------------
    # 1️⃣ Parse Header
    # -----------------------------
    # Example:
    # # Capstone - Bee Hive - Onboarding

    header_line = lines[0].lstrip("# ").strip()
    header_parts = [p.strip() for p in header_line.split("-")]

    if len(header_parts) < 3:
        raise ValueError("Header format incorrect")

    capstone = header_parts[0]
    project = header_parts[1]
    meeting_type = header_parts[2]

    # -----------------------------
    # 2️⃣ Parse Meeting Date
    # -----------------------------
    # Example:
    # **Meeting Date:** 29th Jan, 2026 - 9:01 AM

    date_line = None
    for line in lines:
        if "Meeting Date:" in line:
            date_line = line
            break

    if not date_line:
        raise ValueError("Meeting Date not found")

    date_match = re.search(
        r"\*\*Meeting Date:\*\*\s*(.+?)\s*-\s*(.+)",
        date_line
    )

    if not date_match:
        raise ValueError("Meeting Date format incorrect")

    date = date_match.group(1).strip()
    start_time = date_match.group(2).strip()

    # -----------------------------
    # 3️⃣ Parse Speaker Turns
    # -----------------------------
    # Example:
    # **Hai Jie** *[00:06]*: Hello.

    turn_pattern = re.compile(
        r"\*\*(.+?)\*\*\s*\*\[(.+?)\]\*:\s*(.+)"
    )

    turns = []

    for line in lines:
        match = turn_pattern.match(line.strip())
        if match:
            speaker = match.group(1).strip()
            timestamp = match.group(2).strip()
            text = match.group(3).strip()

            turns.append(
                Turn(
                    speaker=speaker,
                    timestamp=timestamp,
                    text=text
                )
            )

    return Transcript(
        capstone=capstone,
        project=project,
        meeting_type=meeting_type,
        date=date,
        start_time=start_time,
        turns=turns
    )