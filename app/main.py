from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.routers.chamados import router as chamado_router
from app.routers.comentarios import router as comentario_router

app = FastAPI(
    title="HelpDesk API",
    description="API Rest para gerenciamento de chamados de suporte de TI.",
    version="1.0.0"
)



@app.get("/")
def root():
    return {"message": "Bem-vindo ao HelpDesk API!"}

app.include_router (chamado_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(comentario_router)