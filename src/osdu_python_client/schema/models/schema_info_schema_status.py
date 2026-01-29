from enum import Enum


class SchemaInfoSchemaStatus(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    OBSOLETE = "OBSOLETE"
    PUBLISHED = "PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
