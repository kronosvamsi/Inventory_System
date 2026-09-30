import enum

class StatusType(enum.Enum):
    PENDING = "PENDING"
    RECEIVED = "RECEIVED"
    SHIPPED = "SHIPPED"
    APPROVED = "APPROVED"

