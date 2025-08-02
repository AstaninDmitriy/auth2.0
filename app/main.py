from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from app.items.items_views import router as items_router
from users.views import router as users_router
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        yield

app = FastAPI(
    title="MicroShop",
    lifespan=lifespan
)
app.include_router(items_router)
app.include_router(users_router)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
