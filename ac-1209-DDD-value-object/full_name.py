import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

    def __eq__(self, other):
        return (self.first_name == other.first_name) and \
               (self.family_name == other.family_name) and \
               isinstance(other, FullName)


full_name = FullName("matsuoka", "kota")
print(full_name.family_name, full_name.first_name)

full_name = FullName("tanaka", "hiroshi")
print(full_name.family_name, full_name.first_name)
