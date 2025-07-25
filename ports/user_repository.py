from abc import ABC, abstractmethod
from domain.models import UserEntity
from dtos.user_dto import UserRegisterDTO


class UserRepository(ABC):
    @abstractmethod
    def user_exists(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        pass

    @abstractmethod
    def register(self, user: UserRegisterDTO) -> UserEntity:
        pass