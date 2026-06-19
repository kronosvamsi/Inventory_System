""" Orders Table """

from sqlalchemy import String, Integer,Numeric,ForeignKey
from sqlalchemy.orm import  mapped_column, Mapped, relationship

class Order(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(Integer, primary_key =True, index=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"),nullable = False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"),nullable = False)
    product = relationship("Product", back_populates="orders")
    user  = relationship("User",back_populates="orders")
    quantity:Mapped[int] = mapped_column(Integer,nullable = False)
    price:Mapped(float) = mapped_column(Numeric, default=0.0)
