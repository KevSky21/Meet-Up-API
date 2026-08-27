from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.event_id"),nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"),nullable=False)
    created_at = Column(DateTime, default=func.now())