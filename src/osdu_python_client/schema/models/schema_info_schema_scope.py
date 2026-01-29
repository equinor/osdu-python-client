from enum import Enum


class SchemaInfoSchemaScope(str, Enum):
    INTERNAL = "INTERNAL"
    SHARED = "SHARED"

    def __str__(self) -> str:
        return str(self.value)
