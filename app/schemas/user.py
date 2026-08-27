import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    user_id: uuid.UUID
    username: str
    email: EmailStr
    created_at: datetime


    model_config = ConfigDict(from_attributes=True)
