from typing import Union

from ac_1215_DDD_application_service.user import User
from ac_1215_DDD_application_service.user_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def is_duplicated(self, user: User) -> Union[User, None]:
        return self.user_repository.find_by_username(user.username)
