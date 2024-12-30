from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    #These are what we get from the API
    image_url: str
    title: str
    content: str
    creator: str

    #What do we give back to the caller? We have a class post display base model
class PostDisplay(BaseModel):
        id: int 
        image_url: str
        title: str
        content: str
        creator: str
        timestamp: datetime
        class Config():
            orm_mode = True
             