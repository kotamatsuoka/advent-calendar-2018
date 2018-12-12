from __future__ import annotations

import sqlite3
import unittest
import uuid
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

class UserService:
    def is_duplicated(self, user: User) -> bool:
        conn = sqlite3.connect('ddd.db')
        c = conn.cursor()
        t = (user.username.value,)
        c.execute("SELECT * FROM users WHERE username=?", t)
        if c.fetchall() == []:
            return False
        else:
            return True

class Program:
    def creat_user(self, username: str, fist_name:str, family_name: str):
        user = User(UserId(str(uuid.uuid4())),
                    Username(username),
                    FullName(fist_name, family_name))

        user_service =UserService()
        if user_service.is_duplicated(user):
            raise ValueError("重複しています")
        else:
            conn = sqlite3.connect('ddd.db')
            c = conn.cursor()
            t = (user.id.value, user.username.value, user.name.first_name, user.name.family_name)
            c.execute("INSERT INTO users VALUES (?,?,?,?)", t)
            conn.commit()
            conn.close()
