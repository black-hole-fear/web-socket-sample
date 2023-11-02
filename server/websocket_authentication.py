from fastapi import FastAPI, Depends, HTTPException, WebSocket 
from fastapi.security import APIKeyHeader 

app = FastAPI()
api_key_header = APIKeyHeader(name="api_key")

def authenticate_user(api_key: str = Depends(api_key_header)):
    if api_key != "secureapikey":
        raise HTTPException(status_code=401, detail="Unauthorize request!")
    return api_key 

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, api_key: str = Depends(authenticate_user)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You received: {data}")