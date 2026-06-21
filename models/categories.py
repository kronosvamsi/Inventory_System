""" Categories Table """ 

from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import  mapped_column, Mapped , relationship
from db.base import Base

class Category(Base):
    __tablename__ = "categories"
    
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    description:Mapped[str] = mapped_column(String(500),nullable = False)
    products = relationship("Product", back_populates="category")