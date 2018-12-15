import unittest

from DDD_application_service.user import Username, UserId
from DDD_application_service.user_application_service import UserApplicationService
from DDD_application_service.user_repository import InMemoryUserRepository


class TestUserApplicationService(unittest.TestCase):
    def setUp(self):
        self.in_memory_user_repository = InMemoryUserRepository()
        self.user_application_service = UserApplicationService(self.in_memory_user_repository)

    def test_ユーザを登録する(self):
        username = "yuki"

        self.user_application_service.register_user(username, "ゆうき", "まつい")
        actual = self.in_memory_user_repository.find_by_username(Username(username))

        self.assertEqual(username, actual.username.value)

    def test_ユーザを登録する_usernameが重複時は保存できない(self):
        with self.assertRaises(ValueError):
            self.user_application_service.register_user("kota", "こうた", "まつい")

    def test_ユーザ情報を変更する(self):
        new_username = "kotaro"
        new_first_name = "こたろう"
        new_family_name = "まつお"
        target = self.in_memory_user_repository.find_by_username(Username("kota"))
        target_id = target.id.value

        self.user_application_service.change_user_info(target_id, new_username, new_first_name, new_family_name)

        actual = self.in_memory_user_repository.find_by_user_id(UserId(target_id))

        self.assertEqual(new_username, actual.username.value)
        self.assertEqual(new_first_name, actual.name.first_name)
        self.assertEqual(new_family_name, actual.name.family_name)

    def test_ユーザを削除する(self):
        target = self.in_memory_user_repository.find_by_username(Username("kota"))
        target_id = target.id.value
        self.user_application_service.remove_user(target_id)

        actual = self.in_memory_user_repository.find_by_user_id(UserId(target_id))

        self.assertIsNone(actual)

    def test_ユーザ一覧を取得する(self):
        actual = self.user_application_service.find_all()

        target_1 = self.in_memory_user_repository.find_by_username(Username("kota"))
        target_2 = self.in_memory_user_repository.find_by_username(Username("daiki"))

        self.assertEqual(target_1.id.value, actual[0].id)
        self.assertEqual(target_2.id.value, actual[1].id)


if __name__ == "__main__":
    unittest.main()
