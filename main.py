import io
from fastapi import FastAPI, Depends
from starlette.responses import StreamingResponse
from key_generation import generate_keys
from models import User
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from db import get_db

app = FastAPI()
#http://localhost:8000/
origins = [
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""

// http сервис для генерации публичного, возврат в массиве байтов из бд
// например вставка адресса в поле, а из бд достается публ ключ єтого адресса

"""
import coincurve.keys
@app.get("/get_pub_key/{name}")
def get_pk(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.address == name).first()
    if user is None:
        user = generate_keys(name, db)
    return StreamingResponse(io.BytesIO(user.public_key), media_type="application/octet-stream")



