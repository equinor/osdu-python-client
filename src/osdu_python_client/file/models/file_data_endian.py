from enum import Enum


class FileDataEndian(str, Enum):
    BIG = "BIG"
    LITTLE = "LITTLE"

    def __str__(self) -> str:
        return str(self.value)
