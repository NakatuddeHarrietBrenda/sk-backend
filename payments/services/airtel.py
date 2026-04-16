import requests
import uuid

AIRTEL_BASE = "https://openapiuat.airtel.africa"

def airtel_token():
    # simplified (real production uses OAuth)
    return "YOUR_AIRTEL_TOKEN"


def request_airtel_payment(phone, amount):
    token = airtel_token()
    ref = str(uuid.uuid4())

    url = f"{AIRTEL_BASE}/merchant/v1/payments/"

    payload = {
        "reference": ref,
        "subscriber": {
            "country": "UG",
            "currency": "UGX",
            "msisdn": phone
        },
        "transaction": {
            "amount": amount,
            "country": "UG",
            "currency": "UGX",
            "id": ref
        }
    }

    res = requests.post(
        url,
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    return ref, res.status_code, res.text