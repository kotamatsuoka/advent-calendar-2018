import uuid
from abc import ABCMeta, abstractmethod
from typing import Union, List

from DDD_application_service.user import UserId, Username, User, FullName


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_user_id(self, user_id: UserId) -> Union[User, None]:
        pass

    @abstractmethod
    def find_by_username(self, username: Username) -> Union[User, None]:
        pass

    @abstractmethod
    def find_all(self) -> Union[List[User], None]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def remove(self, user: User) -> None:
        pass


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.data = []

        user_id_1 = UserId(str(uuid.uuid4()))
        initial_user = User(user_id_1, Username("kota"), FullName("こうた", "まつおか"))
        self.data.append(initial_user)

        user_id_2 = UserId(str(uuid.uuid4()))
        initial_user_2 = User(user_id_2, Username("daiki"), FullName("だいき", "おおた"))
        self.data.append(initial_user_2)

    def find_by_user_id(self, user_id: UserId) -> Union[User, None]:
        target_user = [user for user in self.data if user.id.value == user_id.value]
        if target_user:
            return target_user[0]
        else:
            return None

    def find_by_username(self, username: Username) -> Union[User, None]:
        target_user = [user for user in self.data if user.username.value == username.value]
        if target_user:
            return target_user[0]
        else:
            return None

    def find_all(self) -> List[User]:
        return self.data

    def save(self, user: User) -> None:
        self.data.append(user)

    def remove(self, user: User) -> None:
        self.data.remove(user)
