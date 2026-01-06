from pydantic import BaseModel

class  UserSchema(BaseModel):
    name:str
    is_active:bool