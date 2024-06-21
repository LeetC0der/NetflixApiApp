from fastapi import FastAPI
from app.api.endpoints.archive import NetflixFileAccessPoint
app = FastAPI()

app.include_router(NetflixFileAccessPoint.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Pandas and NumPy!"}
