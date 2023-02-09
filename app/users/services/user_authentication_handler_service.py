import time
from typing import Dict

import jwt

from app.config import settings


USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def sign_jwt(user_id: str, role: str) -> Dict[str, str]:
    payload = {"user_id": user_id, "role": role, "expires": time.time() + 1800}
    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}


def decode_jwt(token: str) -> Dict:
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(e.__str__())
        return {}
