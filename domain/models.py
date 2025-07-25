from pydantic import BaseModel


class UserEntity(BaseModel):
    username: str
    email: str
