from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# Entrar no virtual environment: .\venv\Scripts\activate.bat
# Start server e update toda vez que salvar codigo: uvicorn main:app --reload
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    isDraft: bool = True

while True: 
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', 
        user='postgres', password='ur97drid', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful")
        break
    except Exception as error:
        print("Connection to database has failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title 1", "content": "content of post 1", "id": 1}, {"title": "comidinhas", "content": "batatinha airfry", "id": 2}]

def find_post(id: int):
    for p in my_posts:
        if p['id'] == id:
            return p

def delete_fun(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            my_posts.pop(i)
            return True
    return False

@app.get("/")
def root():
    return {"message": "salve dudaaa"}

# Ver posts do usuario
@app.get("/posts")
def posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"message": posts}

# Login do usuário
@app.get("/login")
def login():
    return {"message": "login"}

# Novo post
# Estrutura: title (str), content (str), isdraft (bool)
@app.post("/posts", status_code=status.HTTP_201_CREATED) 
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, isdraft) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content, post.isDraft))
    new_post = cursor.fetchone()
    conn.commit()
    return{"data": new_post}

@app.get("/posts/{id}") # id: path parameter
def get_post(id: int): #fastAPI vai extrair o valor em {id}
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    return{"post_detail": post}

# Deletar post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update post
@app.put("/posts/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT)
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, isdraft = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.isDraft, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    return {"data": updated_post}
# Sistema de favoritar posts