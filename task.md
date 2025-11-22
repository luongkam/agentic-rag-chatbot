# Task: Agentic RAG Chatbot for E-commerce

- [x] **Initialization & Setup**
    - [x] Create project structure
    - [x] Set up virtual environment and install dependencies (LangGraph, LangChain, FastAPI, etc.)
    - [x] Configure environment variables (API Keys)

- [x] **Core Agent Architecture (LangGraph)**
    - [x] Define Agent State (messages, context, current_step)
    - [x] Create "Supervisor" or "Router" node to decide intent (General chat vs Product Search vs Order Status)
    - [x] Create "Product Search" node (RAG)
    - [x] Create "Order Support" node (Mock Database)
    - [ ] Implement "Human Handoff" logic (optional but good for "smart")

- [x] **RAG Engine (The "Accurate" Part)**
    - [x] Set up Supabase Client wrapper
    - [x] Create product_search and order_lookup tools
    - [ ] **Ingestion Pipeline** (Future enhancement):
        - [ ] Implement `FileIngestor` for PDF/Docx (using `pypdf` or `unstructured`)
        - [ ] Implement `WebCrawler` for URL training (using `firecrawl` or `beautifulsoup`)
        - [x] Create API endpoint placeholders for uploading documents/links
    - [x] Implement retrieval tool using Supabase Vector Store

- [x] **Customization Layer (The "Easy to Instruct" Part)**
    - [x] Extract system prompts to `app/agent/prompts.py`
    - [ ] Create a `config.yaml` for bot behavior settings (Future)

- [/] **Realtime Voice Layer (The "Wow" Part)**
    - [x] Implement WebSocket endpoint in FastAPI (placeholder)
    - [ ] Integrate OpenAI Realtime API (or Gemini Live) for Audio-to-Audio
    - [x] Implement Frontend Voice Button (basic UI ready)

- [x] **API & Interface (The "Fast" Part)**
    - [x] Build FastAPI backend with streaming support
    - [x] Create a modern, responsive Chat Widget (HTML/JS/Tailwind) for demo

- [ ] **Verification**
    - [ ] Test product queries
    - [ ] Test script customization
    - [ ] Verify latency and accuracy

- [x] **Deployment**
    - [x] Create Dockerfile
    - [x] Create docker-compose.yml
