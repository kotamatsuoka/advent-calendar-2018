import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

    def __post_init__(self):
        if len(self.family_name) > 10:
            raise Exception("10文字以下にしてください。")

full_name = FullName("matsuoka", "kota")
print(full_name.family_name, full_name.first_name)

full_name = FullName("daijoujidani", "hiroshi")
print(full_name.family_name, full_name.first_name)
