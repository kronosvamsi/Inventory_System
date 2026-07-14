from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import mapped_column, Mapped
from db.base import Base
from order_status import StatusType

    

class ProductOrder(Base):
    __tablename__ = "purchase_orders"

    id:Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    supplier:Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    product_id:Mapped[int] = mapped_column(Integer, nullable=False)
    item_name:Mapped[str] = mapped_column(String(50), nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable = False)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status:Mapped[StatusType] = mapped_column(Enum(StatusType), nullable = False)