import sqlite3
from typing import Union

from ac_1213_DDD_repository.user import Username, User, UserId, FullName


class UserRepository:
    def find(self, username: Username) -> Union[User, None]:
        conn = sqlite3.connect('sample.db')
        c = conn.cursor()
        t = (username.value,)
        c.execute("SELECT * FROM users WHERE username=?", t)
        user_tuple = c.fetchone()

        if user_tuple:
            # indexで取得しているのは改良の余地あり
            id = UserId(user_tuple[0])
            username = Username(user_tuple[1])
            fullname = FullName(user_tuple[2], user_tuple[3])

            return User(id, username, fullname)
        else:
            return None

    def save(self, user: User):
        conn = sqlite3.connect('sample.db')
        c = conn.cursor()
        t = (user.id.value, user.username.value, user.name.first_name, user.name.family_name)
        c.execute("INSERT INTO users VALUES (?,?,?,?)", t)
        conn.commit()
        conn.close()

