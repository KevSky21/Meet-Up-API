from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String,unique=True, nullable=False)
    username = Column(String,unique=True, nullable=False)
    password = Column(String,nullable=False)
    birth = Column(Date)
    phone_num = Column(String, nullable=True)
    createdAt = Column(DateTime,default=func.now())

