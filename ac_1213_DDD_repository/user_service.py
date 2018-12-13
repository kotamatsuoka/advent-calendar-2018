from typing import Union

from ac_1213_DDD_repository.user import User
from ac_1213_DDD_repository.user_repository import UserRepository


class UserService:
    def is_duplicated(self, user: User) -> Union[User, None]:
        user_repository = UserRepository()
        return user_repository.find(user.username)
