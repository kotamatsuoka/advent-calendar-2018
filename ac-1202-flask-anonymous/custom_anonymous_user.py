from flask_login import AnonymousUserMixin


class CustomAnonymousUser(AnonymousUserMixin):
    @property
    def id(self):
        return 0

    @property
    def username(self):
        return "Anonymous"

    @property
    def address(self):
        return "earth"

    @property
    def age(self):
        return 99
