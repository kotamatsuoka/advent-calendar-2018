from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class UserStatus:
    username: str
    address: str
    age: int


if __name__ == "__main__":
    user_status = UserStatus("kota", "Nagoya", 23)

    print(user_status)
    print("__repr__(): ", user_status.__repr__())

    user_status_2 = UserStatus("yuki", "Nagoya", 24)

    print("UserStatusインスタンス同士の比較(eq): ", user_status.__eq__(user_status_2))
    print("インスタンス変数の比較(eq): ", user_status.address.__eq__(user_status_2.address))
    print("UserStatusインスタンス同士の比較(lt): ", user_status.__lt__(user_status_2))

    print(user_status.__hash__())

    user_status.address = "Tokyo"
    # => dataclasses.FrozenInstanceError: cannot assign to field 'address'
