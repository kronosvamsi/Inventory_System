""" Instock Table """

from datetime import datetime
from sqlalchemy import Integer,ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped,relationship
from enum import Enum as Snum
from db.base import Base

class TransactionType(str, Snum):
    STOCK_IN = "stock_in"
    STOCK_OUT = "stock_out"
    

class InStock(Base):
    __tablename__ = "in_stock"
    
    id:Mapped[int] = mapped_column(Integer, primary_key = True, index=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"),nullable = False)
    quantity:Mapped[int] = mapped_column(Integer, default=0)
    transaction_type:Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    product = relationship("Product", back_populates = "in_stock")
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable = False)