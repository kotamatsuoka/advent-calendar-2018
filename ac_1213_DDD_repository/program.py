import uuid

from ac_1213_DDD_repository.user import User, UserId, Username, FullName
from ac_1213_DDD_repository.user_repository import UserRepository
from ac_1213_DDD_repository.user_service import UserService


class Program:
    def create_user(self, username: str, fist_name:str, family_name: str):
        user = User(UserId(str(uuid.uuid4())),
                    Username(username),
                    FullName(fist_name, family_name))

        user_service = UserService()
        if user_service.is_duplicated(user):
            raise ValueError("重複しています")
        else:
            user_repository = UserRepository()
            user_repository.save(user)
