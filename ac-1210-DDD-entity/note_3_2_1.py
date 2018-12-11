import dataclasses
import unittest


@dataclasses.dataclass(frozen=True)
class FullName:
    full_name: str


@dataclasses.dataclass
class User:
    def __init__(self, full_name: FullName):
        self.full_name = full_name

    def change_full_name(self, new_name: FullName) -> None:
        if new_name is None:
            raise ValueError(f"{new_name} is invalid argument")

        self.full_name = new_name


class TestUserEntity1(unittest.TestCase):
    def test_属性を変更できる(self):
        user = User(FullName("matsuoka kota"))
        user.change_full_name(FullName("tanaka satoshi"))

        self.assertEqual(FullName("tanaka satoshi"), user.full_name)


if __name__ == "__main__":
    unittest.main()
