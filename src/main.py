from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from config import settings
from crud import router as crud_router
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

app.include_router(crud_router, prefix=settings.api_prefix)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.host,
                port=settings.port,
                reload=True)
