from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(length=60))
    slug = Column(String(length=100))
    description = Column(Text)
    active = Column(Integer)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
    content = Column(Text)
