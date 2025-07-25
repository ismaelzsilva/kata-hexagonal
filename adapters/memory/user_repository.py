from dtos.user_dto import UserRegisterDTO
from domain.models import UserEntity
from ports.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self, users: list[UserEntity]):
        self.users = {user.email: user for user in users}

    def user_exists(self, email: str) -> bool:
        return email in self.users

    def get_by_email(self, email: str) -> UserEntity:
        return UserEntity(
            username=self.users[email].username,
            email=email,
        )
    
    def register(self, user: UserRegisterDTO) -> UserEntity:
        new_user = UserEntity(
            username=user.username,
            email=user.email,
        )
        self.users[user.email] = new_user
        return self.get_by_email(user.email)
