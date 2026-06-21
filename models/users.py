""" Users Table """
from datetime import datetime
from sqlalchemy import String, Integer,Enum, DateTime, func
from enum import Enum as PyEnum
from sqlalchemy.orm import  mapped_column, Mapped, relationship
from db.base import Base
from typing import Literal
from typing import get_args


class RoleStatus(str,PyEnum):
    ADMIN = "admin"
    USER = "user"
    OWNER = "owner"

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    firstname:Mapped[str] = mapped_column(String(100),nullable=False)
    lastname:Mapped[str] = mapped_column(String(100),nullable=False)
    username:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    email:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    address:Mapped[str] = mapped_column(String(100),nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable = False)
    role:Mapped[RoleStatus] = mapped_column(
        Enum(RoleStatus),nullable=False)
    orders = relationship(
        "Order",
        back_populates="user"
    )