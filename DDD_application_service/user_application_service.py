import uuid
from typing import List

from DDD_application_service.user import User, FullName, Username, UserId
from DDD_application_service.user_repository import IUserRepository
from DDD_application_service.user_service import UserService
from DDD_application_service.user_summary_model import UserSummaryModel


class UserApplicationService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        self.user_service = UserService(user_repository)

    def register_user(self, username: str, first_name: str, family_name: str) -> None:
        user = User(UserId(str(uuid.uuid4())), Username(username), FullName(first_name, family_name))

        if self.user_service.is_duplicated(user):
            raise ValueError("重複しています")
        else:
            self.user_repository.save(user)

    def change_user_info(self, user_id: str, username: str, first_name: str, family_name: str) -> None:
        target_id = UserId(user_id)
        target = self.user_repository.find_by_user_id(target_id)

        if target == None:
            raise Exception("not found. target id:" + user_id)

        new_username = Username(username)
        target.change_username(new_username)

        new_full_name = FullName(first_name, family_name)
        target.change_name(new_full_name)

        self.user_repository.save(target)


    def remove_user(self, user_id: str) -> None:
        target_id = UserId(user_id)
        target = self.user_repository.find_by_user_id(target_id)

        if target == None:
            raise Exception("not found. target id:" + user_id)

        self.user_repository.remove(target)

    def find_all(self) -> List[UserSummaryModel]:
        users = self.user_repository.find_all()

        return [UserSummaryModel(user) for user in users]
