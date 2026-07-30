from fastapi import FastAPI
from app.routers.user import router


app = FastAPI(
    title="HelpDesk API",
    description= "API Rest para gerenciamento de chamados de suporte de TI.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Bem-vindo ao HelpDesk API!"}

app.include_router(router)