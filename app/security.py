from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
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

def verificar_admin (usuario_token=Depends(verificar_token)):
    if usuario_token["tipo"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Acesso negado"
        )

    return usuario_token


