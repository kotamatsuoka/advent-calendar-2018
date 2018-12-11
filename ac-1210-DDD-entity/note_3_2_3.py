from __future__ import annotations
import dataclasses
import uuid
import unittest


@dataclasses.dataclass(frozen=True)
class FullName:
    full_name: str


@dataclasses.dataclass(frozen=True)
class UserId:
    value: str


@dataclasses.dataclass
class User:
    full_name: FullName
    id: UserId

    def change_full_name(self, new_name: FullName) -> None:
        if new_name is None:
            raise ValueError(f"{new_name} is invalid argument")

        self.full_name = new_name

    def __eq__(self, other: User):
        # idのみで比較する
        return isinstance(other, User) and (self.id == other.id)


class TestUserEntity3(unittest.TestCase):
    def test_オブジェクトの属性が変化しても同一性が保証される(self):
        tom = User(FullName("Tom Cruise"), UserId(str(uuid.uuid4())))

        before_tom = tom

        tom.change_full_name(FullName("Tom Hanks"))

        self.assertEqual(before_tom, tom)


if __name__ == "__main__":
    unittest.main()
