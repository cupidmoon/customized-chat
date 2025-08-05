from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, TIMESTAMP

from data.model import Base

class ChatRoom(Base):
    __tablename__ = 'chat_room'

    room_id = Column(String, primary_key=True)

    room_type = Column(String, nullable=False)
    room_title = Column(String, nullable=False)
    # user_no = Column(Integer, ForeignKey=('user_info.user_no'))
    user_no = Column(Integer, nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    last_date = Column(TIMESTAMP, nullable=False)

    room_user_infos = relationship("RoomUserInfo", back_populates="room", cascade="all, delete-orphan")
    room_contract_infos = relationship("RoomContractInfo", back_populates="room", cascade="all, delete-orphan")