from pydantic import BaseModel

class post_create(BaseModel):
    title:str
    content:str

class post_response(BaseModel):
    title:str
    content:str