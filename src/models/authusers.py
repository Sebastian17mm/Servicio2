from pydantic import BaseModel, Field
from typing import Optional

class AuthUsersModel(BaseModel):
    encryptedToken: Optional[str] = ''
    internalId:  Optional[str] = ''