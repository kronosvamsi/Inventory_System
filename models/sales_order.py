from datetime import datetime
from sqlalchemy import Integer, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .order_status import StatusType
from db.base import Base


class SalesOrder(Base):

    __tablename__ = "sales_order"
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id:Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"), nullable = False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status:Mapped[StatusType] = mapped_column(Enum(StatusType), nullable=False)
    customer = relationship("Customer", back_populates = "sales_order")
    product = relationship("Product", back_populates = "sales_order")