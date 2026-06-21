""" Orders Table """
from datetime import datetime
from sqlalchemy import String, Integer,Numeric,ForeignKey,DateTime,func
from sqlalchemy.orm import  mapped_column, Mapped, relationship
from db.base import Base

class Order(Base):
    __tablename__ = "orders"
    
    id:Mapped[int] = mapped_column(Integer, primary_key =True, index=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"),nullable = False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"),nullable = False)
    product = relationship("Product", back_populates="orders")
    user  = relationship("User",back_populates="orders")
    quantity:Mapped[int] = mapped_column(Integer,nullable = False)
    price:Mapped[float] = mapped_column(Numeric, default=0.0)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable = False)
    
