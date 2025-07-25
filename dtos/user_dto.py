from pydantic import BaseModel


class UserRegisterDTO(BaseModel):
    username: str
    email: str