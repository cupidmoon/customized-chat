from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, TIMESTAMP

from data.model import Base

class RoomUserInfo(Base):
    __tablename__ = 'room_user_info'

    room_id = Column(String, ForeignKey('chat_room.room_id'), primary_key=True)
    info_key = Column(String, primary_key=True)
    info_value = Column(String, nullable=False)
    sort_order = Column(Integer)

    # room = relationship("ChatRoom", back_populates="room_user_infos")
