from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import user, post, auth, vote
from config import settings

# Entrar no virtual environment: .\venv\Scripts\activate.bat
# Start server e update toda vez que salvar codigo: uvicorn main:app --reload
# desativar venv: deactivate

print(settings.database_username)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"] # -> Wildcard * libera todos os domínios, quando for lançar o site, colocar a lista de origens adequadas

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "main"}

# @app.get("/login")
# def login():
#     return {"message": "login"}