from enum import Enum


class WorkflowRunResponseStatus(str, Enum):
    FAILED = "FAILED"
    INPROGRESS = "INPROGRESS"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    SUBMITTED = "SUBMITTED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
