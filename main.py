from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pipeline import run_rag_pipeline

app = FastAPI()

class QueryRequest(BaseModel):
    user_id: str
    query: str

@app.post("/query")
def query_endpoint(request: QueryRequest):
    if not request.user_id or not request.query:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    response = run_rag_pipeline(request.user_id, request.query)
    return {"response": response}
