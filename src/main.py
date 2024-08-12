from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from config import settings
from database import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)
router = APIRouter()
app.include_router(router, prefix=settings.api_prefix)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.host,
                port=settings.port,
                reload=True)
