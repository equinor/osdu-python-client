class OsduError(Exception):
    pass


class OsduConfigError(OsduError):
    pass


class OsduAuthError(OsduError):
    pass


class OsduRetryExhausted(OsduError):
    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
