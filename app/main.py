from fastapi import FastAPI, WebSocket, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import json
import asyncio

from app.agent.graph import graph
from langchain_core.messages import HumanMessage

app = FastAPI(title="Agentic RAG Chatbot")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = "default"

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint that processes user messages through the LangGraph agent.
    """
    inputs = {"messages": [HumanMessage(content=request.message)]}
    config = {"configurable": {"thread_id": request.thread_id}}
    
    # Run the graph
    # For streaming, we would use graph.astream
    # For simplicity in this first pass, we use invoke
    try:
        result = await graph.ainvoke(inputs, config=config)
        last_message = result["messages"][-1]
        return {"response": last_message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ws/realtime")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for Realtime Audio-to-Audio.
    Currently a placeholder for the OpenAI Realtime API integration.
    """
    await websocket.accept()
    try:
        while True:
            # Receive audio/text from client
            data = await websocket.receive_text()
            
            # Logic to forward to OpenAI Realtime API would go here
            # For now, just echo back
            await websocket.send_text(f"Echo: {data}")
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file (PDF/Docx) for ingestion.
    """
    # Placeholder for Ingestion Service
    return {"filename": file.filename, "status": "Uploaded (Mock)"}

@app.post("/crawl")
async def crawl_url(url: str):
    """
    Crawl a URL for training.
    """
    # Placeholder for Web Crawler
    return {"url": url, "status": "Crawling started (Mock)"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
