import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from config import settings

app = FastAPI()
router = APIRouter()
app.include_router(router, prefix=settings.api_prefix)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.host,
                port=settings.port,
                reload=True)
