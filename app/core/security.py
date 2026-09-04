from jose import jwt
import uuid
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id: uuid.UUID, expires_in_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:

    expires_time = datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)

    payload = {
        "sub": str(user_id),                 #user ID
        "exp": expires_time,                 #expiration
        "iat": datetime.now(timezone.utc),   #issued at
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token