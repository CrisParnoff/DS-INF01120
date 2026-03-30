from fastapi import FastAPI
from Routes.interface_route import router as interface_router

app = FastAPI()

app.include_router(interface_router)