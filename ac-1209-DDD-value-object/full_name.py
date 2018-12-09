import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

fullname1 = FullName("matsuoka", "kota")
print(fullname1.family_name)
