from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UsersSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    customId: str = Field(...)
    fname: str = Field(...)
    lname: str = Field(...)
    age:   str = Field(...)
    address: str = Field(...)
    tel: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
        
