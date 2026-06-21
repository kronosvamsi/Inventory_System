"""  Products Table """

from datetime import datetime
from sqlalchemy import String, Integer, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import  mapped_column, Mapped,relationship
from db.base import Base

class Product(Base):
    __tablename__ = "products"
    
    id:Mapped[int] =   mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id:Mapped[int] = mapped_column(ForeignKey("categories.id"),nullable=False)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    sku:Mapped[str] =  mapped_column(String(50), unique=True)
    quantity:Mapped[int] = mapped_column(Integer,default=0)
    price:Mapped[float] = mapped_column(Numeric(10,2))
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default= func.now(), nullable = False)
    category = relationship(
        "Category",
        back_populates="products"
    )

    orders = relationship(
        "Order",
        back_populates="product"
    )

    in_stock = relationship(
        "InStock",
        back_populates="product"
    )

