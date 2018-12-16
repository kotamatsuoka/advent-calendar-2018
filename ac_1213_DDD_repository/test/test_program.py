import sqlite3
import unittest
import uuid

from ac_1213_DDD_repository.program import Program
from ac_1213_DDD_repository.user import Username
from ac_1213_DDD_repository.user_repository import UserRepository


class TestProgram(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE users(id text, username text, first_name text, family_name text)""")
        users = [(str(uuid.uuid4()), "kota", "こうた", "まつおか"), (str(uuid.uuid4()), "kazuo", "かずお", "まつい")]
        c.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
        conn.commit()
        conn.close()

    def tearDown(self):
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()
        c.execute("""DROP TABLE users""")
        conn.commit()
        conn.close()

    def test_usernameが重複時は保存できない(self):
        with self.assertRaises(ValueError):
            Program().create_user("kota", "こうた", "まつい")

    def test_usernameが重複していない時は保存してそのusernameが一件だけ存在するか(self):
        username = "yuki"
        Program().create_user(username, "ゆうき", "まつい")

        conn = sqlite3.connect('sample.db')
        c = conn.cursor()
        t = (username,)
        c.execute("SELECT * FROM users WHERE username=?", t)

        self.assertEqual(1, c.fetchall().__len__())

    def test_usernameでUserを検索する(self):
        username = Username("kota")

        user_repository = UserRepository()
        actual = user_repository.find(username)

        self.assertEqual("kota", actual.username.value)

if __name__ == "__main__":
    unittest.main()
