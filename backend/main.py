from fastapi import FastAPI

from api.routes import router
from database.db import engine
from database.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Autonomous Content Pipeline")

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Autonomous Content Pipeline API Running"
    }