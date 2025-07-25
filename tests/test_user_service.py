import pytest
from unittest.mock import Mock

from application.user_service import UserService
from domain.models import UserEntity
from dtos.user_dto import UserRegisterDTO
from adapters.memory.user_repository import InMemoryUserRepository


class TestUserService:

    def test_register_user_success(self):
        # Arrange

        repo = InMemoryUserRepository(
            users=[
                UserEntity(username="Nadie", email="nadie@example.com")
            ]
        )

        user_service = UserService(repo)

        new_user = UserRegisterDTO(username="Ismael", email="ismael@example.com")

        # Act
        result = user_service.register_user(new_user)

        # Assert
        assert result.username == "Ismael"
        assert result.email == "ismael@example.com"

    def test_register_user_already_exists(self):
        # Arrange

        repo = InMemoryUserRepository(
            users=[
                UserEntity(username="Ismael", email="ismael@example.com")
            ]
        )

        user_service = UserService(repo)

        new_user = UserRegisterDTO(username="Ismael", email="ismael@example.com")

        # Act and Assert
        with pytest.raises(
            ValueError, match="El usuario ya existe con mismo email"
        ):
            user_service.register_user(new_user) 