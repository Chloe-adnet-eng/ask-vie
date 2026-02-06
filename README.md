# ask-vie
A RAG-based assistant that lets clients ask questions and get answers about their Business France VIE contract. It retrieves information from the contract documents.
## Installation and Environment Setup

### Prerequisites
- **Python 3.11+** (required by the project)
- **Poetry** ([installation guide](https://python-poetry.org/docs/#installation))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ask-vie
   ```

2. **Create and activate the virtual environment**
   ```bash
   poetry install
   poetry shell
   ```

## Development Roadmap

### Step 1: Document Loading & Embedding (Current)
Load PDF contracts and generate embeddings locally.

**Success criteria:**
- ✅ Load a PDF document
- ✅ Generate embeddings for chunks
---

*Next steps: Vector store setup → Retriever implementation → LLM integration → Chat interface*
