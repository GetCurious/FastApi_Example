# model / schema (not to be confused with SQLAlchemy's models)

# think TypeScript Interface 

from typing import List

from pydantic import BaseModel


# Item
class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        # SQLAlchemy has "Lazy Loading" enabled by default
        orm_mode = True
        # orm_mode enables method getter automatically
        # eg. id = data.id


# User
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
