# from typing_extensions import TypedDict
from pydantic import BaseModel
from typing import List, Optional

class ContractDetail(BaseModel):
    type: str
    category: str
    name: str
    amount: int
    duration: Optional[str] = None
    status: str
    filter: List[str]
    is_checked: bool

class Contract(BaseModel):
    contract_id: str
    contractor: str
    product: str
    start_date: str
    end_date: str
    maturity_age: str
    payment_schedule: str
    fee: int
    payment_count: str
    payment_rate: str
    is_checked: bool
    contract_detail: Optional[List[ContractDetail]] = None

class Analysis(BaseModel):
    covered: int
    canceled: int
    uncovered: int
    lack: int
    fullfillment: int

class ContractAnalysis(BaseModel):
    customer_id: str
    customer_name: str
    analysis_date: str
    total_fee: int
    analysis: Analysis
    contracts: Optional[List[Contract]] = None