from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "seeds_dataset"

    area = Column(Float, primary_key=True, index=True)
    perimter = Column(Float, index=True)
    compactness = Column(Float, index=True)
    length = Column(Float, index=True)
    width = Column(Float, index=True)
    asymmetry = Column(Float, index=True)
    groove = Column(Float, index=True)
    item_class = Column(Integer, index=True)
