from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import sqlapp.crud as crud, sqlapp.models as models, sqlapp.schemas as schemas
from sqlapp.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/class/{item_class}", response_model=list[schemas.Item])
def get_class(item_class: int, db: Session = Depends(get_db)):
    classes = crud.get_class(db, item_class=item_class)        
    return classes



