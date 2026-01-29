from enum import Enum


class MemberDtoRole(str, Enum):
    MEMBER = "MEMBER"
    OWNER = "OWNER"

    def __str__(self) -> str:
        return str(self.value)
