from sqlalchemy import Column
from sqlalchemy import ForeignKey
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import enum
from sqlalchemy import Enum

class RSVPstatus(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    declined = "declined"

class Participant(Base):

    __tablename__ = "participant"

    user_id = Column(UUID(as_uuid=True),ForeignKey("users.user_id"), primary_key=True)
    status = Column(Enum(RSVPstatus), default=RSVPstatus.pending)
    event_id = Column(UUID(as_uuid=True),ForeignKey('events.event_id'), primary_key=True)

