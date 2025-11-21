# Implementation Plan - Agentic RAG Chatbot

## Goal Description
Xây dựng một chatbot bán hàng thông minh (Agentic RAG) đáp ứng các tiêu chí:
1.  **Thông minh nhất**: Sử dụng kiến trúc **LangGraph** để quản lý luồng hội thoại phức tạp, có khả năng suy luận và gọi công cụ (tools).
2.  **Phản hồi nhanh nhất**: Sử dụng **FastAPI** với Streaming Response và **Gemini 1.5 Flash** (hoặc model tương đương) để tối ưu tốc độ.
3.  **Chính xác nhất**: Kết hợp **RAG (Retrieval Augmented Generation)** sử dụng **Supabase (pgvector)** để tra cứu thông tin sản phẩm và đơn hàng chính xác.
4.  **Dễ hướng dẫn & Custom**: Tách biệt logic code và kịch bản (prompts). Người dùng có thể chỉnh sửa file `config.yaml` và các file prompt markdown để thay đổi hành vi bot mà không cần sửa code.

## User Review Required
> [!IMPORTANT]
> Cần cung cấp **Supabase URL** và **Supabase Key**, cùng với API Key của LLM.

## Proposed Changes

### Backend Structure (Python)
#### [NEW] `app/main.py`
- Entry point của FastAPI server.
- Endpoints:
    - `POST /chat`: Chat text (Streaming).
    - `WS /realtime`: **WebSocket cho hội thoại giọng nói thời gian thực (Audio-to-Audio)**. Kết nối với OpenAI Realtime API hoặc Gemini Live.
    - `POST /upload`: Upload tài liệu.
    - `POST /crawl`: Gửi URL.

#### [NEW] `app/agent/graph.py` (The Brain)
- **Supervisor Agent**: Phân loại intent.
- **Sales Agent**: Tư vấn bán hàng (RAG).
- **Support Agent**: CSKH.
- **Realtime Handler**: Xử lý luồng audio, VAD (Voice Activity Detection) và function calling trong thời gian thực.

#### [NEW] `app/services/ingestion.py` (The Knowledge Base)
- Xử lý đa định dạng (PDF/Docx/URL).
- Chunking & Embedding vào Supabase.

#### [NEW] `app/agent/tools.py`
- `product_search`: Tìm kiếm vector.
- `order_lookup`: Tra cứu đơn hàng.

#### [NEW] `app/rag/supabase_client.py`
- Quản lý kết nối Supabase.

#### [NEW] `config/prompts/`
- `system.md`: Kịch bản chính.
- `realtime_instructions.md`: Kịch bản tối ưu cho giọng nói (ngắn gọn, tự nhiên hơn).

### Frontend (Demo)
#### [NEW] `frontend/index.html`
- Chat Widget (Text).
- **Voice Mode**: Nút "Call" để bắt đầu hội thoại giọng nói (WebRTC/WebSocket).
- **Admin Panel**: Upload file/link.

## Verification Plan

### Automated Tests
- Script test các trường hợp:
    - Hỏi về sản phẩm có trong database -> Trả về đúng thông tin.
    - Hỏi về sản phẩm không có -> Trả lời không biết hoặc gợi ý khác.
    - Yêu cầu kiểm tra đơn hàng -> Gọi đúng tool.

### Manual Verification
- Chạy server và chat thử trên giao diện web.
- Thử thay đổi file prompt và verify bot thay đổi cách nói chuyện.
