import dataclasses


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

    def __eq__(self, other):
        return (self.first_name == other.first_name) and \
               (self.family_name == other.family_name) and \
               isinstance(other, FullName)


full_name1 = FullName("matsuoka", "kota")
full_name2 = FullName("tanaka", "hiroshi")
print(full_name1 == full_name1)
print(full_name1 == full_name2)
