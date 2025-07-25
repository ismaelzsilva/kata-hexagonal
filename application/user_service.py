from domain.models import UserEntity
from dtos.user_dto import UserRegisterDTO
from ports.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_data: UserRegisterDTO) -> UserEntity:
        if self.user_repository.user_exists(user_data.email):
            raise ValueError("El usuario ya existe con mismo email")
        
        return self.user_repository.register(user_data)

    def get_user_by_email(self, email: str) -> UserEntity:
        if not self.user_repository.user_exists(email):
            raise ValueError("Usuario no encontrado")
        
        return self.user_repository.get_by_email(email)