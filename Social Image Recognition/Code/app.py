from fastapi import FastAPI, Query
from main import main
import asyncio

app = FastAPI()

# Create a lock to ensure that the requests are processed one by one
lock = asyncio.Lock()

@app.get("/")
def root():
    return ("Server is up")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {"message": "Favicon not available"}

@app.get("/imagerecog")
async def read_item(id: int = Query(...), endpoint: str = Query(...)):

    async with lock:  # Ensure only one request is processed at a time

        response = main(id, endpoint)

        if isinstance(response, list):
            return {"success": "true", "message": "Prediction successful", "result": response}
        
        else:
            return {"success": "false", "message": response, "result": "[]"}

