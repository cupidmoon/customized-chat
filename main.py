from fastapi import FastAPI
from typing import List, Optional

from contract.contracts import Contract, ContractDetail, ContractAnalysis, Analysis
from users.userinfo import UserInfo, UserDetail

app = FastAPI()

@app.get("/contract/filters")
def read_contract_filters():
    """
    상품 보장 분류 필터 항목 조회
    """
    return {"filters": ["암", "뇌/심장", "치료비", "수술비", "입원일당", "실비", "운전자", "치아"]}

@app.get("/user/infos")
def read_user_info():
    """
    고객 정보 항목 조회
    """
    return [
        {"key": "성별", "order": 1},
        {"key": "나이", "order": 2},
        {"key": "직업", "order": 3},
        {"key": "병력", "order": 4},
        {"key": "희망 보험료", "order": 5}
    ]

@app.get("/contract/{customer_id}")
def read_contract_analysis(customer_id: str) -> ContractAnalysis:
    """
    고객의 보장 분석 데이터 조회
    """
    return ContractAnalysis(
        customer_id=customer_id,
        customer_name="John Doe",
        analysis_date="2023-10-01",
        total_fee=218040,
        analysis=Analysis(
            covered=2,
            canceled=0,
            uncovered=1,
            lack=0,
            fullfillment=80
        ),
        contracts=[
            Contract(
                contract_id="contract_1",
                contractor="Shinhan Life Insurance",
                product="Brave Orange Whole Life Insurance (Non-dividend, Low Surrender Value Type)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/20년",
                fee=218040,
                payment_count="93/240",
                payment_rate="38%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_2",
                contractor="KDB Life Insurance",
                product="(Non) Essential 2 Major Adult Disease Coverage Insurance Type 1 Non-renewal",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="80세",
                payment_schedule="월납/20년",
                fee=218040,
                payment_count="83240",
                payment_rate="34%",
                is_checked=True,
                contract_detail=[
                    ContractDetail(
                        type="Indemnity",
                        category="Fracture Diagnosis",
                        name="Fracture Diagnosis Fee (Excluding Teeth)",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accidental Death",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 80%↑",
                        name="Outpatient Medical Expenses (Disease)",
                        amount=8000000,
                        status="Normal",
                        filter=["치료비", "입원일당", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Fixed",
                        category="Burn Diagnosis",
                        name="Burn Diagnosis Fee",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "수술비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Other",
                        name="Disability Pension for 80%+ Injury During Public Transport",
                        amount=30000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    )
                ]
            ),
            Contract(
                contract_id="contract_3",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Actual Medical Expense Insurance (2004.5) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/10년",
                fee=46612,
                payment_count="23/36",
                payment_rate="63%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_4",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Smart Customized Coverage Insurance (2004.6) (Renewal Contract) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/20년",
                fee=46612,
                payment_count="23/36",
                payment_rate="63%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_5",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Smart Customized Coverage Insurance (2004.6) (Renewal Contract) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/20년",
                fee=35063,
                payment_count="21/36",
                payment_rate="58%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_6",
                contractor="Meritz Fire & Marine Insurance",
                product="(Non) Meritz The Good Right Dental Insurance 2501",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/5년",
                fee=44430,
                payment_count="1/60",
                payment_rate="1%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_7",
                contractor="Hyundai Marine & Fire Insurance",
                product="Non-dividend New Hi-Car Driver Accident Insurance (Hi2310) Type 1 (Driver) Basic Plan",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/5년",
                fee=30000,
                payment_count="17/240",
                payment_rate="7%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_8",
                contractor="Hyundai Marine & Fire Insurance",
                product="Non-dividend Hyundai Happiness Full Life Security Insurance (Hi20404) Type 1 (Annual Maturity) Basic Plan",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/5년",
                fee=30000,
                payment_count="12/240",
                payment_rate="5%",
                is_checked=True
            )
     ])

@app.post("/room")
def begin_chat(contract_analysis: ContractAnalysis, user_info: Optional[UserInfo] = None):
    """
    대화 시작하기
    """
    if user_info:
        return {"message": f"Contract details with user info {user_info.user_name}"}
    else:
        return {"message": "Contract details without user info"}

@app.get("/room/{room_id}/userinfo")
def read_user_info(room_id: str) -> UserInfo:
    """
    Get user information in the chat room.
    """
    return UserInfo(
        user_id="user123",
        user_name="John Doe",
        user_details=[
            UserDetail(key="성별", value="남성", order=1),
            UserDetail(key="나이", value="30", order=2),
            UserDetail(key="직업", value="회사원", order=3),
            UserDetail(key="병력", value="없음", order=4),
            UserDetail(key="희망 보험료", value="10000", order=5)
        ]
    )

@app.get("/room/{room_id}/contract")
def read_contract(room_id: str) -> ContractAnalysis:
    """
    Get contract details in the chat room.
    """
    return ContractAnalysis(
        customer_id="customer_id",
        customer_name="John Doe",
        analysis_date="2023-10-01",
        total_fee=218040,
        analysis=Analysis(
            covered=2,
            canceled=0,
            uncovered=1,
            lack=0,
            fullfillment=80
        ),
        contracts=[
            Contract(
                contract_id="contract_1",
                contractor="Shinhan Life Insurance",
                product="Brave Orange Whole Life Insurance (Non-dividend, Low Surrender Value Type)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/20년",
                fee=218040,
                payment_count="93/240",
                payment_rate="38%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_2",
                contractor="KDB Life Insurance",
                product="(Non) Essential 2 Major Adult Disease Coverage Insurance Type 1 Non-renewal",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/20년",
                fee=218040,
                payment_count="83240",
                payment_rate="34%",
                is_checked=True,
                contract_detail=[
                    ContractDetail(
                        type="Indemnity",
                        category="Fracture Diagnosis",
                        name="Fracture Diagnosis Fee (Excluding Teeth)",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accidental Death",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 80%↑",
                        name="Outpatient Medical Expenses (Disease)",
                        amount=8000000,
                        status="Normal",
                        filter=["치료비", "입원일당", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Fixed",
                        category="Burn Diagnosis",
                        name="Burn Diagnosis Fee",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "수술비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Other",
                        name="Disability Pension for 80%+ Injury During Public Transport",
                        amount=30000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    )
                ]
            ),
            Contract(
                contract_id="contract_3",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Actual Medical Expense Insurance (2004.5) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="종신",
                payment_schedule="월납/10년",
                fee=46612,
                payment_count="23/36",
                payment_rate="63%",
                is_checked=True,
                contract_detail=[
                    ContractDetail(
                        type="Indemnity",
                        category="Fracture Diagnosis",
                        name="Fracture Diagnosis Fee (Excluding Teeth)",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accidental Death",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 3%↑",
                        name="Accidental Death & Disability",
                        amount=2000000,
                        status="Normal",
                        filter=["운전자", "치료비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Accident Disability 80%↑",
                        name="Outpatient Medical Expenses (Disease)",
                        amount=8000000,
                        status="Normal",
                        filter=["치료비", "입원일당", "실비", "수술비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Fixed",
                        category="Burn Diagnosis",
                        name="Burn Diagnosis Fee",
                        amount=200000,
                        status="Normal",
                        filter=["치료비", "수술비", "실비"],
                        is_checked=True
                    ),
                    ContractDetail(
                        type="Indemnity",
                        category="Other",
                        name="Disability Pension for 80%+ Injury During Public Transport",
                        amount=30000000,
                        status="Normal",
                        filter=["운전자", "치료비", "입원일당"],
                        is_checked=True
                    )
                ]
            ),
            Contract(
                contract_id="contract_4",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Smart Customized Coverage Insurance (2004.6) (Renewal Contract) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/20년",
                fee=46612,
                payment_count="23/36",
                payment_rate="63%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_5",
                contractor="Samsung Fire & Marine Insurance",
                product="Samsung Fire Direct Smart Customized Coverage Insurance (2004.6) (Renewal Contract) (Non-dividend)",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/20년",
                fee=35063,
                payment_count="21/36",
                payment_rate="58%",
                is_checked=True
            ),
            Contract(
                contract_id="contract_6",
                contractor="Meritz Fire & Marine Insurance",
                product="(Non) Meritz The Good Right Dental Insurance 2501",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/5년",
                fee=44430,
                payment_count="1/60",
                payment_rate="1%",
                is_checked=False
            ),
            Contract(
                contract_id="contract_7",
                contractor="Hyundai Marine & Fire Insurance",
                product="Non-dividend New Hi-Car Driver Accident Insurance (Hi2310) Type 1 (Driver) Basic Plan",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/5년",
                fee=30000,
                payment_count="17/240",
                payment_rate="7%",
                is_checked=False
            ),
            Contract(
                contract_id="contract_8",
                contractor="Hyundai Marine & Fire Insurance",
                product="Non-dividend Hyundai Happiness Full Life Security Insurance (Hi20404) Type 1 (Annual Maturity) Basic Plan",
                start_date="2023-10-01",
                end_date="2024-10-01",
                maturity_age="60세",
                payment_schedule="월납/5년",
                fee=30000,
                payment_count="12/240",
                payment_rate="5%",
                is_checked=False
            )
        ]
    )

@app.put("/room/{room_id}/userinfo", response_model=None)
def update_user_info(room_id: str, user_info: UserInfo):
    """
    Update user information in the chat room.
    """
    return {"message": f"User info for room {room_id} updated successfully."}

@app.put("/room/{room_id}/contract")
def update_contract(room_id: str, contract: ContractAnalysis):
    """
    Update contract details in the chat room.
    """
    return {"message": f"Contract details for room {room_id} updated successfully."}