from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict

# Base schema con los campos comunes
class AuthorBase(BaseModel):
    name: str
    email: str

# Schema para crear un autor
class AuthorCreate(AuthorBase):
    pass

# Schema para respuesta de autor
class Author(AuthorBase):
    id: int

    class Config:
        from_attributes: True
