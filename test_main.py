from fastapi.testclient import TestClient
from main import app
from contract.contracts import Analysis, Contract, ContractDetail, ContractAnalysis
from users.userinfo import UserInfo, UserDetail

client = TestClient(app)

def test_read_contract_filters():
    response = client.get("/contract/filters")
    print("test_read_contract_filters response:", response.json())
    assert response.status_code == 200
    
    data = response.json()
    assert "filters" in data
    assert isinstance(data["filters"], list)
    assert "암" in data["filters"]

def test_read_user_info():
    response = client.get("/user/infos")
    print("test_read_user_info response:", response.json())
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert all("key" in item and "order" in item for item in data)

def test_read_contract_analysis():
    response = client.get("/contract/testuser")
    print("test_read_contract_analysis response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert "customer_id" in data
    assert "contracts" in data
    assert isinstance(data["contracts"], list)


def test_begin_chat_without_userinfo():
    sample_body = ContractAnalysis(
        customer_id="user123",
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
            )
        ]
    )
    response = client.post("/room", json={"contract_analysis": sample_body.model_dump()})
    assert response.status_code == 200
    assert response.json()["message"] == "Contract details without user info"

def test_begin_chat_with_userinfo():
    sample_body = ContractAnalysis(
        customer_id="user123",
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
            )
        ]
    )
    sample_user = UserInfo(
        user_id="user123",
        user_name="John Doe",
        user_details=[
            UserDetail(key="성별", value="남성", order=1),
            UserDetail(key="나이", value="35", order=2),
        ]
    )

    response = client.post("/room", json={"contract_analysis": sample_body.model_dump(),
                                          "user_info": sample_user.model_dump()})
    assert response.status_code == 200
    assert response.json()["message"] == "Contract details with user info John Doe"

def test_update_user_info():
    sample_user = UserInfo(
        user_id="user123",
        user_name="John Doe",
        user_details=[
            UserDetail(key="성별", value="남성", order=1),
            UserDetail(key="나이", value="35", order=2),
            UserDetail(key="직업", value="정비사", order=3),
            UserDetail(key="병력", value="고혈압", order=4),
            UserDetail(key="희망 보험료", value="월 30만원", order=5)
        ]
    )
    response = client.put("/room/room1/userinfo", json=sample_user.model_dump())
    print("test_update_user_info response:", response.json())
    assert response.status_code == 200
    assert "message" in response.json()
