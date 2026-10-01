from pydantic import BaseModel

class SupplierData(BaseModel):
    name : str 
    supplier_type : str
    address : str
    city : str
    state : str
    pincode : str
    email : str
    phone : str

class SupplierResponse(BaseModel):
    id:int
    name : str 
    supplier_type : str
    email : str
