from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Event(Base):
    __tablename__ = "events"

    event_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    location = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    #User doesn't have to have a limit. Should say no limit if not included
    maxParty = Column(Integer, nullable=True)