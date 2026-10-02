from pydantic import BaseModel, ConfigDict

class CustomerData(BaseModel):
    name : str
    customer_type : str
    address: str
    city: str
    state: str
    pincode: str
    email: str
    phone:str

class CustomerResponse(BaseModel):
    id : int
    name : str
    customer_type : str
    email: str

    model_config = ConfigDict(from_attributes = True)
    