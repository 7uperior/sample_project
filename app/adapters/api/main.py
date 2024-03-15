from fastapi import FastAPI

from app.adapters.api import router
from app.config.database import init_db

app = FastAPI()


@app.on_event('startup')
async def startup_event():
	await init_db()


app.include_router(router)
