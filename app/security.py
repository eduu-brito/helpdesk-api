from fastapi.security import HTTPBearer
from fastapi import Depends
from app.core.config import ALGORITHM, SECRET_KEY
import jwt

security = HTTPBearer()

def verificar_token (credentials = Depends(security)):
    payload = jwt.decode (
        credentials.credentials,
        SECRET_KEY,
        algorithms= [ALGORITHM]
    )
    return payload
