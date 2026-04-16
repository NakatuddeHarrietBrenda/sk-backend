import requests
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("MTN_BASE_URL")
SUB_KEY = os.getenv("MTN_SUB_KEY")
USER_ID = os.getenv("MTN_USER_ID")
API_KEY = os.getenv("MTN_API_KEY")


def get_token():
    url = f"{BASE_URL}/collection/token/"
    res = requests.post(
        url,
        auth=(USER_ID, API_KEY),
        headers={"Ocp-Apim-Subscription-Key": SUB_KEY}
    )
    return res.json().get("access_token")


def request_to_pay(phone, amount):
    token = get_token()
    reference_id = str(uuid.uuid4())

    url = f"{BASE_URL}/collection/v1_0/requesttopay/{reference_id}"

    body = {
        "amount": str(amount),
        "currency": "UGX",
        "externalId": reference_id,
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": phone
        },
        "payerMessage": "Rent Payment",
        "payeeNote": "SK Property"
    }

    res = requests.put(
        url,
        json=body,
        headers={
            "Authorization": f"Bearer {token}",
            "X-Reference-Id": reference_id,
            "X-Target-Environment": "sandbox",
            "Ocp-Apim-Subscription-Key": SUB_KEY
        }
    )

    return reference_id, res.status_code, res.text