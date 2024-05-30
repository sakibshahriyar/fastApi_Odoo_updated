from pydantic import BaseModel

class Partner(BaseModel):
    name: str
    email: str
    phone: str
