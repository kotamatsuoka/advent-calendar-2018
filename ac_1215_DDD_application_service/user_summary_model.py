from ac_1215_DDD_application_service.user import User


class UserSummaryModel:
    def __init__(self, user: User):
        self.id = user.id.value
        self.first_name = user.name.first_name
