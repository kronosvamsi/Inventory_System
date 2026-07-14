""" Supplier Table """

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base

class Supplier(Base):
    
    __tablename__ = "suppliers"
    
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String(50), nullable = False)
    supplier_type:Mapped[str] = mapped_column(String(50), nullable = False)
    address:Mapped[str] = mapped_column(String(100),nullable = True)
    city:Mapped[str] = mapped_column(String(50),nullable = False)
    state:Mapped[str] = mapped_column(String(50),nullable = False)
    pincode:Mapped[int] = mapped_column(Integer,nullable = False)
    email:Mapped[str] = mapped_column(String(50), nullable = False)
    phone:Mapped[str] = mapped_column(String(20), nullable = False)