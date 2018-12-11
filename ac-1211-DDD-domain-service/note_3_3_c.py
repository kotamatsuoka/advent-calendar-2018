from __future__ import annotations
import unittest
import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: str


@dataclass(frozen=True)
class Username:
    username: str


@dataclass
class User:
    user_id: UserId
    username: Username


class UserService:
    def is_duplicated(self, user: User) -> bool:
        # 自らのユーザのみ重複判断できる
        return user.username in USER_LIST


# DB代わりのリスト
USER_LIST = [Username("松岡"), Username("松田"), Username("松井")]


class TestUserService(unittest.TestCase):
    def test_ユーザーが重複しているかをドメインサービスに任せる(self):
        matsuoka = User(UserId(str(uuid.uuid4())), Username("松岡"))

        self.assertTrue(UserService().is_duplicated(matsuoka))


if __name__ == "__main__":
    unittest.main()
