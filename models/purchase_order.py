from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from db.base import Base
from .order_status import StatusType

    

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id:Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    supplier_id:Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable = False)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status:Mapped[StatusType] = mapped_column(Enum(StatusType), nullable = False)
    supplier = relationship("Supplier",back_populates="purchase_order")
    product = relationship("Product", back_populates = "purchase_order")