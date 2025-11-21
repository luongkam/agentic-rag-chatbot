# High-Level Architecture: Agentic RAG Chatbot

Dưới đây là sơ đồ kiến trúc tổng thể của hệ thống (dạng văn bản).

```text
[ USER (Client) ]
       |
       | (1) HTTP POST (Text Chat)
       | (2) WebSocket (Realtime Voice)
       v
+-----------------------------------------------------------------------+
|  BACKEND (FastAPI)                                                    |
|                                                                       |
|  [ API Gateway ] <-----> [ WebSocket Handler ]                        |
|         |                        |                                    |
|         v                        v                                    |
|  +-----------------------------------------------------------------+  |
|  |  AGENTIC BRAIN (LangGraph)                                      |  |
|  |                                                                 |  |
|  |  [ Supervisor / Router ] ------------------------------------+  |  |
|  |         |                   |                 |              |  |  |
|  |         v                   v                 v              |  |  |
|  |  [ Sales Agent ]     [ Support Agent ]  [ Realtime Handler ] |  |  |
|  |   (Tư vấn bán hàng)   (Tra cứu đơn)      (Xử lý giọng nói)   |  |  |
|  +-----------------------------------------------------------------+  |
|         |                   |                 |                       |
+---------|-------------------|-----------------|-----------------------+
          |                   |                 |
          | (3) RAG Search    | (4) SQL Query   | (5) Audio Stream
          v                   v                 v
+---------------------+  +-----------+    +--------------------------+
| KNOWLEDGE BASE      |  | DATABASE  |    | EXTERNAL AI SERVICES     |
| (Supabase Vector)   |  | (Supabase)|    |                          |
|                     |  |           |    | [ LLM (Gemini/OpenAI) ]  |
| [ Product Vectors ] |  | [ Orders ]|    | [ Realtime Voice API ]   |
| [ Doc Vectors ]     |  |           |    |                          |
+---------------------+  +-----------+    +--------------------------+

(6) INGESTION PIPELINE (Admin Panel)
    [ PDF/Docx/URL ] ---> [ Ingestion Service ] ---> [ Supabase Vector ]
```

## Giải thích luồng dữ liệu:

1.  **Chat Text**:
    *   User gửi tin nhắn -> **API Gateway**.
    *   **Supervisor** phân tích ý định (Intent).
    *   Nếu hỏi sản phẩm -> Chuyển **Sales Agent** -> Tra cứu **Supabase Vector** -> Trả lời.
    *   Nếu hỏi đơn hàng -> Chuyển **Support Agent** -> Tra cứu **Supabase Database** -> Trả lời.

2.  **Realtime Voice**:
    *   User nói -> **WebSocket Handler**.
    *   **Realtime Handler** stream âm thanh tới **External Voice API** (OpenAI/Gemini).
    *   Nhận phản hồi âm thanh và phát lại cho User ngay lập tức.

3.  **Training (Ingestion)**:
    *   Admin upload file/link -> **Ingestion Service** xử lý -> Lưu vào **Supabase Vector**.
