from sqlalchemy.orm import Session
from . import models, schemas

def get_class(db: Session, item_class: int):
    print(f"Sql count: {db.query(models.Item).filter(models.Item.item_class == item_class).count()}")
    return db.query(models.Item).filter(models.Item.item_class == item_class).all()