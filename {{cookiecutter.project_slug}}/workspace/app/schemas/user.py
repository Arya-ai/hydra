from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl


# Shared Properties
class UserBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserBaseInDB(UserBase):
    id: int = None

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBaseInDB):
    password: Optional[str] = None


# Additional properties to return via API
class User(UserBaseInDB):
    pass


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
