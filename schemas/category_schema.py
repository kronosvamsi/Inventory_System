from pydantic import BaseModel, ConfigDict

class CategoryInput(BaseModel):
    id:int
    name:str
    description:str

class CategoryResponse(BaseModel):
    id:int
    name:str
    description:str

    model_config = ConfigDict(from_attributes = True)

class CategoryUpdate(BaseModel):
    name:str
    description:str
