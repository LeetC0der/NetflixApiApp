from fastapi import FastAPI
from app.api.endpoints.archive import NetflixFileAccessPoint
from app.api.endpoints.director import Director
app = FastAPI()

app.include_router(NetflixFileAccessPoint.router)
app.include_router(Director.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Pandas and NumPy!"}
