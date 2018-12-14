from typing import Union

from ac_1214_DDD_test_repository.in_memory_user_reposiotry import IUserRepository
from ac_1214_DDD_test_repository.user import User


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def is_duplicated(self, user: User) -> Union[User, None]:
        return self.user_repository.find(user.username)
