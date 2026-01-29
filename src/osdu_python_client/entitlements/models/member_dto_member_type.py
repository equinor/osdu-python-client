from enum import Enum


class MemberDtoMemberType(str, Enum):
    GROUP = "GROUP"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
