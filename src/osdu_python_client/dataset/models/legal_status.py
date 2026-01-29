from enum import Enum


class LegalStatus(str, Enum):
    COMPLIANT = "compliant"
    INCOMPLIANT = "incompliant"

    def __str__(self) -> str:
        return str(self.value)
