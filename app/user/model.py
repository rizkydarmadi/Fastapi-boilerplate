from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(length=50))
    midle_name = Column(String(length=50))
    last_name = Column(String(length=50))
    mobile = Column(String(length=24))
    email = Column(String(length=24))
    password_hash = Column(String(length=128))
    registered_at = Column(DateTime(timezone=True))
    last_login = Column(DateTime(timezone=True))
    intro = Column(Text)
    profile = Column(Text)
    role_id = Column(ForeignKey("role.id"), nullable=False)

    role = relationship("Role")
