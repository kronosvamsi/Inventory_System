from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from db.base import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(50),nullable = False)
    customer_type:Mapped[str] = mapped_column(String(50),nullable = False)
    address:Mapped[str] = mapped_column(String(100),nullable = True)
    city:Mapped[str] = mapped_column(String(50),nullable = False)
    state:Mapped[str] = mapped_column(String(50),nullable = False)
    pincode:Mapped[int] = mapped_column(Integer,nullable = False)
    email:Mapped[str] = mapped_column(String(60),nullable = False)
    phone:Mapped[str] = mapped_column(String(20), nullable = False)
    sales_order = relationship("SalesOrder", back_populates="customer")
