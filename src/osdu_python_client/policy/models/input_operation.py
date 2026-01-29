from enum import Enum


class InputOperation(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    PURGE = "purge"
    UPDATE = "update"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
