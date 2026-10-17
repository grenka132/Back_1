from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database

app = FastAPI()

# Простая функция для получения сессии БД
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item(name: str, db: Session = Depends(get_db)):
    new_item = models.Item(name=name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item