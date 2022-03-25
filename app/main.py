from fastapi import FastAPI

from .sub_app import views as sub_app
from .sub_app2 import views as sub_app2

app = FastAPI()

app.include_router(sub_app.router)
app.include_router(sub_app2.router)


@app.get("/")
async def root():
    return {"msg": "Hello World"}
