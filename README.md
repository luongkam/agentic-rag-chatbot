# Agentic RAG Chatbot

> **Smart, Fast, Accurate, and Customizable** e-commerce chatbot powered by LangGraph and Supabase.

## 🎯 Features Implemented

✅ **Core Agent Architecture (LangGraph)**
- Supervisor Agent for intelligent routing
- Sales Agent with RAG capabilities
- Support Agent for order lookups
- Clean state management

✅ **RAG Engine**
- Supabase integration (ready for pgvector)
- Product search tool
- Order lookup tool
- Mock data for testing without Supabase

✅ **API & Interface**
- FastAPI backend with async support
- Modern chat widget (HTML/TailwindCSS)
- WebSocket endpoint for Realtime Voice (placeholder)
- CORS enabled for frontend access

✅ **Deployment**
- Dockerized application
- docker-compose for easy deployment
- Ready for production

## 🚀 Quick Start

### Option 1: Using Docker (Recommended)

```bash
# 1. Configure environment variables
cp .env.example .env
# Edit .env and add your API keys

# 2. Start the application
docker-compose up --build

# 3. Access the chat widget
# Open frontend/index.html in your browser
```

### Option 2: Manual Setup

```bash
# 1. Install Python 3.10+
# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env

# 4. Run the server
python app/main.py

# 5. Open frontend/index.html
```

## 📋 Environment Variables

Required in `.env`:

```bash
# LLM API Key (choose one or both)
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AIza...

# Supabase (optional for now, mock data works without it)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=eyJ...
```

## 🏗️ Architecture

```
Frontend (HTML/JS) 
    ↓ HTTP/WebSocket
Backend (FastAPI)
    ↓
Supervisor Agent (LangGraph)
    ├→ Sales Agent → RAG Search → Supabase Vector
    ├→ Support Agent → Order Lookup → Supabase DB
    └→ General Chat → LLM
```

## 📁 Project Structure

```
├── app/
│   ├── main.py              # FastAPI server
│   ├── agent/
│   │   ├── state.py         # LangGraph state
│   │   ├── graph.py         # Workflow definition
│   │   ├── nodes.py         # Agent logic
│   │   ├── prompts.py       # System prompts
│   │   └── tools.py         # RAG tools
│   └── rag/
│       └── supabase_client.py  # Supabase wrapper
├── frontend/
│   └── index.html           # Chat UI
├── config/
│   └── prompts/             # Future: External prompts
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## ✅ Current Status (as of 2025-11-22)

- [x] Core Agent Architecture
- [x] RAG Tools (with mock data)
- [x] FastAPI Backend
- [x] Frontend Chat Widget
- [x] Docker Deployment
- [ ] Ingestion Pipeline (PDF/URL)
- [ ] Realtime Voice Integration
- [ ] Full Supabase Setup

## 🧪 Testing

Try these queries in the chat:
- "Hello" → General chat
- "Show me cameras" → Sales Agent (mock products)
- "Check order #123" → Support Agent

## 🔜 Next Steps

1. **Set up Supabase**
   - Create project
   - Enable pgvector extension
   - Create tables for products and documents

2. **Implement Ingestion Pipeline**
   - File upload (PDF/Docx)
   - URL crawler

3. **Realtime Voice**
   - Integrate OpenAI Realtime API
   - Add audio recording to frontend

## 📝 License

MIT
