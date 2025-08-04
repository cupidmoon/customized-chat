# from typing_extensions import TypedDict
from pydantic import BaseModel
from typing import List, Optional

class UserDetail(BaseModel):
    key: str
    value: str
    order: Optional[int]

class UserInfo(BaseModel):
    user_id: str
    user_name: str
    user_details: Optional[List[UserDetail]]
