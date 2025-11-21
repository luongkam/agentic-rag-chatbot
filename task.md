# Task: Agentic RAG Chatbot for E-commerce

- [x] **Initialization & Setup**
    - [x] Create project structure
    - [x] Set up virtual environment and install dependencies (LangGraph, LangChain, FastAPI, etc.)
    - [x] Configure environment variables (API Keys)

- [ ] **Core Agent Architecture (LangGraph)**
    - [ ] Define Agent State (messages, context, current_step)
    - [ ] Create "Supervisor" or "Router" node to decide intent (General chat vs Product Search vs Order Status)
    - [ ] Create "Product Search" node (RAG)
    - [ ] Create "Order Support" node (Mock Database)
    - [ ] Implement "Human Handoff" logic (optional but good for "smart")

- [ ] **RAG Engine (The "Accurate" Part)**
    - [ ] Set up Supabase Project & Enable `pgvector` extension
    - [ ] Create tables for Products and Documents (Vectors)
    - [ ] **Ingestion Pipeline**:
        - [ ] Implement `FileIngestor` for PDF/Docx (using `pypdf` or `unstructured`)
        - [ ] Implement `WebCrawler` for URL training (using `firecrawl` or `beautifulsoup`)
        - [ ] Create API endpoint for uploading documents/links
    - [ ] Implement retrieval tool using Supabase Vector Store

- [ ] **Customization Layer (The "Easy to Instruct" Part)**
    - [ ] Extract system prompts to `prompts/` directory
    - [ ] Create a `config.yaml` for bot behavior settings

- [ ] **Realtime Voice Layer (The "Wow" Part)**
    - [ ] Implement WebSocket endpoint in FastAPI
    - [ ] Integrate OpenAI Realtime API (or Gemini Live) for Audio-to-Audio
    - [ ] Implement Frontend Audio Recorder & Player (AudioWorklet)

- [ ] **API & Interface (The "Fast" Part)**
    - [ ] Build FastAPI backend with streaming support
    - [ ] Create a modern, responsive Chat Widget (HTML/JS/Tailwind) for demo

- [ ] **Verification**
    - [ ] Test product queries
    - [ ] Test script customization
    - [ ] Verify latency and accuracy
