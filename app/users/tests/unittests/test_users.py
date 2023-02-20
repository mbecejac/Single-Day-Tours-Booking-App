import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.exceptions import UserNotFoundException
from app.users.repositories import UserRepository


class TestUserRepository(TestClass):
    def create_users_for_methods(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user1@gmail.com", "sifra123")
            user = user_repository.create_user("user2@gmail.com", "sifra123")
            user = user_repository.create_user("user3@gmail.com", "sifra123")
            user = user_repository.create_user("user4@gmail.com", "sifra123")
            print(type(user))

    def test_create_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("testing_user@test.te", "pass12345")
            assert user.email == "testing_user@test.te"
            assert user.is_superuser is False
            assert user.is_active is True

    def test_create_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("testing_user@test.te", "pass12345")
            assert user.email == "testing_user@test.te"
            assert user.is_superuser is not True
            assert user.is_active is not False
            with pytest.raises(IntegrityError):
                user_repository.create_user("testing_user@test.te", "pass12345")

    def test_create_super_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user("testing_user@test.te", "pass12345")
            assert super_user.email == "testing_user@test.te"
            assert super_user.is_superuser is True
            assert super_user.is_active is True

    def test_create_super_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user("testing_user@test.te", "pass12345")
            assert super_user.email == "testing_user@test.te"
            assert super_user.is_superuser is not False
            assert super_user.is_active is not False
            with pytest.raises(IntegrityError):
                user_repository.create_user("testing_user@test.te", "pass12345")

    def test_read_all_users_if_none(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.read_all_users()
            assert all_users == []

    def test_read_all_users(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.read_all_users()
            assert len(all_users) == 4

    def test_read_all_users_error(self):
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.read_all_users()
            assert not len(all_users) != 4

    def test_read_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            user1 = user_repository.read_user_by_id(user.id)
            assert user1 is not None
            with pytest.raises(UserNotFoundException):
                user_repository.read_user_by_id("false_user_id")

    def test_read_user_by_email(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            assert user is not None
            user1 = user_repository.read_user_by_email("user@gmail.com")
            assert user.email == user1.email
            with pytest.raises(UserNotFoundException):
                user_repository.read_user_by_email("false_user_email")

    def test_user_is_active(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            assert user.is_active is True
            user_repository.update_user_is_active(user.id, is_active=False)
            assert user.is_active is False

    def test_user_is_active_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            assert user.is_active is True
            user_repository.update_user_is_active(user.id, is_active=False)
            assert user.is_active is not True

    def test_user_is_superuser(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            assert user.is_superuser is False
            user_repository.update_user_is_superuser(user.id, is_superuser=True)
            assert user.is_superuser is True

    def test_delete_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "sifra1253")
            assert user is not None
            with pytest.raises(UserNotFoundException):
                user = user_repository.read_user_by_id("false_id")
            user_delete = user_repository.delete_user_by_id(user.id)
            assert user_delete is True
