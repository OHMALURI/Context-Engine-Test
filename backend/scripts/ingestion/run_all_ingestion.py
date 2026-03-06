import subprocess
import sys

PYTHON_EXE = sys.executable

print("Starting Full Ingestion Pipeline\n")

print("Running Transcript Ingestion...")
subprocess.run([PYTHON_EXE, "transcript_ingest.py"])

print("\nRunning Scope Document Ingestion...")
subprocess.run([PYTHON_EXE, "Scope_ingest.py"])

print("\nAll ingestion completed.")