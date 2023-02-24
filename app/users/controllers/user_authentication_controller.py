"""User authentication controller"""
from typing import List

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.users.services import decode_jwt


class JWTBearer(HTTPBearer):
    """HTTPBearer subclass checks for a valid JWT token with a specified role"""

    def __init__(self, role: List[str], auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid or expired token.")
            if payload.get("role") not in self.role:
                raise HTTPException(status_code=403, detail="User is not permitted to access this route.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    # @staticmethod
    # def verify_jwt(jwtoken: str) -> dict:
    #     """Verifies a JWT token"""
    #     is_token_valid: bool = False
    #     try:
    #         payload = decode_jwt(jwtoken)
    #     except Exception as e:
    #         payload = None
    #         print(e)
    #     if payload:
    #         is_token_valid = True
    #     return {"valid": is_token_valid, "role": payload["role"]}

    def verify_jwt(self, jwtoken: str) -> dict:
        try:
            payload = decode_jwt(jwtoken)
        except Exception:
            payload = None
        if payload:
            if payload.get("role") is not None:
                return {"valid": True, "role": payload["role"]}
        return {"valid": False}
