from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: str

@dataclass(frozen=True)
class Username:
    value: str

@dataclass(frozen=True)
class FullName:
    first_name: str
    family_name: str

@dataclass
class User:
    id: UserId
    username: Username
    name: FullName

    def change_username(self, new_username: Username):
        self.username = new_username

    def change_name(self, new_name: FullName):
        self.name = new_name

    def __eq__(self, other: User):
        # idのみで比較する
        return isinstance(other, User) and (self.id == other.id)
