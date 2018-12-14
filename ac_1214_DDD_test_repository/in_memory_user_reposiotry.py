import uuid
from typing import Union

from ac_1214_DDD_test_repository.user import UserId, FullName


class IUserRepository:
    def find(self, username: Username) -> Union[User, None]:
        pass

    def save(self, user: User):
        pass


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.data = []

        user_id = UserId(str(uuid.uuid4()))
        initial_user = User(user_id, Username("kota"), FullName("こうた", "まつい"))
        self.data.append({user_id: initial_user})

    def find(self, username: Username) -> Union[User, None]:
        # もう少しきれいに書けるはず
        target_user = [user for user in self.data if list(user.values())[0].username.value == username.value]
        if target_user:
            return list(target_user[0].values())[0]
        else:
            return None

    def save(self, user: User) -> None:
        self.data.append({user.id: user})
