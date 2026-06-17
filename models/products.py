"""  Products Table """

from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import  mapped_column, Mapped
from db.base import Base

class Product(Base):
    __tablename__ = "products"
    id:Mapped[int] =   mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    sku:Mapped[str] =  mapped_column(String(50), unique=True)
    quantity:Mapped[int] = mapped_column(Integer,default=0)
    price:Mapped[float] = mapped_column(Numeric(10,2))

