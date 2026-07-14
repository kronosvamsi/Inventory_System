from sqlalchemy import Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from order_status import StatusType


class SalesOrder(Base):

    __tablename__ = "sales_order"
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer:[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    product_id:[int] = mapped_column(Integer, nullable = False)
    quantity:[int] = mapped_column(Integer, nullable=False, default=0)
    status:[StatusType] = mapped_column(Enum(StatusType), nullable=False)