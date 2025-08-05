from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from data.model import Base

class UserInfoTemplate(Base):
    __tablename__ = 'user_info_template'
    
    info_key = Column(String, primary_key=True)
    info_name = Column(String, nullable=False)
    sort_order = Column(Integer)
    is_active = Column(Boolean, nullable=False, default=True)

    values = relationship("CodeInfo", back_populates="key", cascade="all, delete-orphan")