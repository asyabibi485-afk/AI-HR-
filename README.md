# 🎓 Enterprise College HR Policy AI Assistant

A beginner-friendly AI assistant for answering questions from Enterprise College HR policy documents.

## Current Stage

**Stage 1 - HR Policy Document Loading**

The application currently:

- Loads PDF files
- Loads DOCX files
- Loads TXT files
- Extracts text
- Displays document information
- Shows a document preview

## Project Structure

```text
hr-policy-ai-assistant/
├── app.py
├── document_loader.py
├── requirements.txt
├── README.md
└── data/
    └── Put your HR policy files here
```

## Run Locally

Install requirements:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

## API Key

No API key is required for Stage 1.

The Gemini API key will be added later when the RAG chatbot is connected to the AI model. Never commit an API key to GitHub.

## Next Stages

1. Document chunking
2. Embeddings
3. FAISS vector database
4. RAG retrieval
5. Gemini AI chatbot
6. Streamlit UI improvements
7. GitHub and Streamlit deployment
