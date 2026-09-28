from pydantic import BaseModel, ConfigDict,Field

class CategoryCreate(BaseModel):
    name:str = Field(min_length = 1, max_length = 50)
    description:str = Field(min_length = 1, max_length = 150)

class CategoryResponse(BaseModel):
    id:int
    name:str
    description:str

    model_config = ConfigDict(from_attributes = True)

class CategoryUpdate(BaseModel):
    name:str =  Field(min_length = 1, max_length = 50)
    description:str = Field(min_length = 1, max_length = 150)
