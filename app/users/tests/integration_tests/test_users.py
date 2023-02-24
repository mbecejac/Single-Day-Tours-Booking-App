import json

from app.tests import TestClass, client
from app.users.services import UserService


class TestUserRoute(TestClass):
    @staticmethod
    def setup_super_user():
        UserService.create_super_user("user111@example.com", "string111")

        response = client.post(url="/api/users/login", json={"email": "user111@example.com", "password": "string111"})
        token = response.json()["access_token"]
        return token

    def test_create_super_user(self):
        token = self.setup_super_user()

        response = client.post(
            url="/api/users/add-new-super-user",
            json={"email": "user222@example.com", "password": "pass123"},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert response.status_code == 200
        user = response.json()
        assert user["email"] == "user222@example.com"
        assert user["is_superuser"] is True

    def test_create_user(self):
        token = self.setup_super_user()

        response = client.post(
            url="/api/users/add-new-user",
            json={"email": "user333@example.com", "password": "pass123"},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert response.status_code == 200
        user = response.json()
        assert user["email"] == "user333@example.com"
        assert user["is_superuser"] is False

    def test_get_all_users_if_only_super_user(self):
        token = self.setup_super_user()
        response = client.get(url="/api/users/get-all-users", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        all_users = response.json()
        assert len(all_users) == 1  # 1 superuser

    def test_get_all_users(self):
        token = self.setup_super_user()
        input_user_1 = {"email": "user1@example.com", "password": "pass123"}
        input_user_2 = {"email": "user2@example.com", "password": "pass123"}
        user_1 = client.post(
            url="/api/users/add-new-user",
            content=json.dumps(input_user_1),
            headers={"Authorization": f"Bearer {token}"},
        )
        user_2 = client.post(
            url="/api/users/add-new-user",
            content=json.dumps(input_user_2),
            headers={"Authorization": f"Bearer {token}"},
        )

        assert user_1.status_code == 200
        assert user_2.status_code == 200
        response = client.get(url="/api/users/get-all-users", headers={"Authorization": f"Bearer {token}"})
        all_users = response.json()
        assert len(all_users) == 3  # 2 created users + 1 superuser

    def test_get_user_by_id(self):
        token = self.setup_super_user()
        input_user_1 = {"email": "user1@example.com", "password": "pass123"}
        user_1_create = client.post(
            url="/api/users/add-new-user",
            content=json.dumps(input_user_1),
            headers={"Authorization": f"Bearer {token}"},
        )
        assert user_1_create.status_code == 200
        user_1 = user_1_create.json()
        user_1_id = {"user_id": user_1["id"]}

        response = client.get(
            url="/api/users/get-user/id", params=user_1_id, headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        assert response.json() == user_1

    def test_get_user_by_email(self):
        token = self.setup_super_user()
        input_user_1 = {"email": "user1@example.com", "password": "pass123"}
        user_1_create = client.post(
            url="/api/users/add-new-user",
            content=json.dumps(input_user_1),
            headers={"Authorization": f"Bearer {token}"},
        )
        assert user_1_create.status_code == 200
        user_1 = user_1_create.json()
        user_1_email = {"email": user_1["email"]}

        response = client.get(
            url="/api/users/get-user/email", params=user_1_email, headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        assert response.json() == user_1

    def test_delete_user_by_id(self):
        token = self.setup_super_user()
        input_user_1 = {"email": "user1@example.com", "password": "pass123"}
        user_1_create = client.post(
            url="/api/users/add-new-user",
            content=json.dumps(input_user_1),
            headers={"Authorization": f"Bearer {token}"},
        )
        assert user_1_create.status_code == 200
        user_1 = user_1_create.json()
        user_1_id = {"user_id": user_1["id"]}

        response = client.delete(
            url="/api/users/delete-user", params=user_1_id, headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
