from fastapi import FastAPI

from .database import engine
from .models import tutorial
from .routers import tutorials

tutorial.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tutorials.router)
