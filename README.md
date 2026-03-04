# Context Engine Test

RAG system for processing meeting transcripts using vector embeddings and semantic search.

## Features

- Transcript Parsing: Parse markdown meeting transcripts with speaker identification
- Semantic Chunking: Split conversations into manageable chunks
- Vector Embeddings: OpenAI text-embedding-3-small integration
- Vector Database: Milvus for storing and searching embeddings
- Ingestion Pipeline: Automated processing of transcript files

## Project Structure

<img width="597" height="511" alt="image" src="https://github.com/user-attachments/assets/a37a181e-8453-4de2-b67e-3f9ffaef609f" />


## Setup

Prerequisites:
- Python 3.8+
- Docker Desktop
- OpenAI API key

Installation:

1. Clone repository

git clone https://github.com/OHMALURI/Context-Engine-Test.git
cd Context-Engine-Test

2. Install dependencies

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3. Configure API key

Create backend/.env file:

OPENAI_API_KEY=your-key-here

4. Start Milvus

cd docker
docker-compose up -d
docker ps | grep milvus

## Usage

Run ingestion pipeline:

cd backend
python scripts/ingestion/transcript_ingest.py

This will:
1. Parse all .md files in Data/Transcripts/
2. Split into chunks
3. Generate embeddings via OpenAI
4. Store in Milvus database

Test parser:

python test_parser.py

## Transcript Format

# Capstone - Project Name - Meeting Type

**Meeting Date:** 29th Jan, 2026 - 9:01 AM

**Speaker** *[00:06]*: Hello.
**Another** *[00:08]*: Hi there.

## Docker & Milvus

Start:
docker-compose up -d

Stop:
docker-compose stop

Restart:
docker-compose restart

View logs:
docker-compose logs -f

Port: localhost:19530
Data: Stored in docker/volumes/ (not in Git)

## Database Schema

Collection: meeting_embeddings

Field         Type                Description
id            INT64               Auto-generated
embedding     FLOAT_VECTOR[1536]  Semantic vector
text          VARCHAR(5000)       Chunk with metadata

## Dependencies

openai
pymilvus
python-dotenv
numpy

## Troubleshooting

Milvus connection error:
docker-compose restart

OpenAI API error:
- Check API key in .env
- Verify credits: https://platform.openai.com/usage

Reset Milvus:
docker-compose down
rm -rf volumes/
docker-compose up -d

## Security

Never commit:
- backend/.env (API keys)
- backend/venv/ (virtual environment)
- docker/volumes/ (database files)

These are protected by .gitignore.

## License

MIT

Python 3.8+
Docker Desktop
OpenAI API key

Installation
1. Clone repository
bashgit clone https://github.com/OHMALURI/Context-Engine-Test.git
cd Context-Engine-Test
2. Install dependencies
bashcd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Configure API key
Create backend/.env:
envOPENAI_API_KEY=your-key-here
4. Start Milvus
bashcd docker
docker-compose up -d
docker ps | grep milvus
📖 Usage
Run ingestion pipeline:
bashcd backend
python scripts/ingestion/transcript_ingest.py
This will:

Parse all .md files in Data/Transcripts/
Split into chunks
Generate embeddings via OpenAI
Store in Milvus database

Test parser:
bashpython test_parser.py
📝 Transcript Format
markdown# Capstone - Project Name - Meeting Type

**Meeting Date:** 29th Jan, 2026 - 9:01 AM

**Speaker** *[00:06]*: Hello.
**Another** *[00:08]*: Hi there.
🐳 Docker & Milvus
bash# Start
docker-compose up -d

# Stop
docker-compose stop

# Restart
docker-compose restart

# View logs
docker-compose logs -f
```

**Port**: `localhost:19530`  
**Data**: Stored in `docker/volumes/` (not in Git)

## 🗄️ Database Schema

**Collection**: `meeting_embeddings`

| Field | Type | Description |
|-------|------|-------------|
| id | INT64 | Auto-generated |
| embedding | FLOAT_VECTOR[1536] | Semantic vector |
| text | VARCHAR(5000) | Chunk with metadata |

## 📦 Dependencies
```
openai
pymilvus
python-dotenv
numpy
🐛 Troubleshooting
Milvus connection error:
bashdocker-compose restart
OpenAI API error:

Check API key in .env
Verify credits: https://platform.openai.com/usage

Reset Milvus:
bashdocker-compose down
rm -rf volumes/
docker-compose up -d
🔐 Security
⚠️ Never commit:

backend/.env (API keys)
backend/venv/ (virtual environment)
docker/volumes/ (database files)

These are protected by .gitignore.
