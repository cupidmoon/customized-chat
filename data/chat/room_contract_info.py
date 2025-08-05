from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, TIMESTAMP, JSON

from data.model import Base

class RoomContractInfo(Base):
    __tablename__ = 'room_contract_info'

    room_id = Column(String, ForeignKey('chat_room.room_id'), primary_key=True)
    contract_detail = Column(JSON, nullable=False)

    # room = relationship("ChatRoom", back_populates="room_contract_infos")
