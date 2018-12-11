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

    def is_duplicated(self) -> bool:
        # 自らのユーザのみ重複判断できる
        return self.username in USER_LIST


# DB代わりのリスト
USER_LIST = [Username("松岡"), Username("松田"), Username("松井")]


class TestDomainService(unittest.TestCase):
    def test_ユーザが自らのユーザ名の重複判断ができる(self):
        matsuoka = User(UserId(str(uuid.uuid4())), Username("松岡"))

        self.assertTrue(matsuoka.is_duplicated())


if __name__ == "__main__":
    unittest.main()
