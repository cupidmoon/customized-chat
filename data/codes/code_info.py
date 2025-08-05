from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from data.model import Base

class CodeInfo(Base):
    __tablename__ = 'code_info'

    info_key = Column(String, ForeignKey('user_info_template.info_key'), primary_key=True)
    info_code = Column(String, nullable=False, primary_key=True)
    info_value = Column(String, nullable=False)
    sort_order = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    # key = relationship("UserInfoTempate", back_populates="values")