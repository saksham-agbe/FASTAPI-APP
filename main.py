import sys

import uvicorn
from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    version="1.0.0",
)

sys.dont_write_bytecode = True

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {
        "success": True,
        "message": "Welcome to FastAPI"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
