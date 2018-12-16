import uuid

from ac_1214_DDD_test_repository.in_memory_user_reposiotry import IUserRepository
from ac_1214_DDD_test_repository.user import User, UserId, Username, FullName
from ac_1214_DDD_test_repository.user_service import UserService


class Program:
    def create_user(self, username: str, fist_name:str, family_name: str, user_repository: IUserRepository):
        user_repository = user_repository
        user = User(UserId(str(uuid.uuid4())),
                    Username(username),
                    FullName(fist_name, family_name))

        user_service = UserService(user_repository)
        if user_service.is_duplicated(user):
            raise ValueError("重複しています")
        else:
            user_repository.save(user)
