import unittest

from ac_1214_DDD_test_repository.in_memory_user_reposiotry import InMemoryUserRepository
from ac_1214_DDD_test_repository.program import Program
from ac_1214_DDD_test_repository.user import Username


class TestProgram(unittest.TestCase):
    def test_usernameが重複時は保存できない(self):
        in_memory_user_repository = InMemoryUserRepository()
        with self.assertRaises(ValueError):
            Program().creat_user("kota", "こうた", "まつい", in_memory_user_repository)

    def test_usernameが重複していない時は保存してそのusernameが一件だけ存在するか(self):
        username = "yuki"
        in_memory_user_repository = InMemoryUserRepository()

        Program().creat_user(username, "ゆうき", "まつい", in_memory_user_repository)
        actual = in_memory_user_repository.find(Username(username))

        self.assertEqual(username, actual.username.value)


if __name__ == "__main__":
    unittest.main()
