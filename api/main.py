
from fastapi import FastAPI
from api.routes import logs

app = FastAPI(title="AI IAM Access Manager")

app.include_router(logs.router)
