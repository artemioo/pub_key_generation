import io

from fastapi import FastAPI, Depends
from starlette.responses import StreamingResponse

from key_generation import generate_keys
from models import User
from sqlalchemy.orm import Session

from db import get_db

app = FastAPI()


@app.get("/{address}")
def get_pk(address: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.address == address).first()
    if user is None:
        user = generate_keys(address, db)
    result = bytearray(user.public_key, encoding='utf-8')
    return StreamingResponse(io.BytesIO(result), media_type="application/octet-stream")


