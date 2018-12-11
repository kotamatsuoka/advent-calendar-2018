import dataclasses
import unittest
import uuid


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


class TestUserEntity2(unittest.TestCase):
    def test_同じ属性でも区別される(self):
        tom1 = User(FullName("Tom Cruise"), UserId(str(uuid.uuid4())))
        tom2 = User(FullName("Tom Cruise"), UserId(str(uuid.uuid4())))

        self.assertNotEqual(tom1, tom2)


if __name__ == "__main__":
    unittest.main()
