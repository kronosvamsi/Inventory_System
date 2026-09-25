from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped,relationship
from db.base import Base

class Inventory(Base):
    __tablename__ = "inventories"
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True,index = True,autoincrement= True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False, unique = True)
    quantity_available:Mapped[int] = mapped_column(Integer, default=0,nullable= False)
    reorder_level:Mapped[int] = mapped_column(Integer, default =10,nullable=False)
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable = False,onupdate= func.now())
    product = relationship("Product", back_populates="inventory")

