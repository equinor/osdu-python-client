from enum import Enum


class UpdateWorkflowRunRequestStatus(str, Enum):
    FAILED = "failed"
    FINISHED = "finished"
    QUEUED = "queued"
    RUNNING = "running"
    SUBMITTED = "submitted"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
