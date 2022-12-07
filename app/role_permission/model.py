from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class RolePermission(Base):
    __tablename__ = "role_permission"

    id = Column(Integer, primary_key=True, nullable=False)
    role_id = Column(ForeignKey("role.id"), nullable=False)
    permission_id = Column(ForeignKey("permission.id"), nullable=False)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

    role = relationship("Role")
    permission = relationship("Permission")
