from msal import ConfidentialClientApplication

from tests.config import CoreConfig


class MsalTokenRefresher():
    """TokenRefresher based on MSAL"""

    def __init__(self, core_config: CoreConfig):
        super().__init__()
        self._config = core_config
        self._app = ConfidentialClientApplication(
            self._config.client_id, self._config.client_secret, self._config.authority
        )

    def refresh_token(self):
        result = self._app.acquire_token_for_client(scopes=[self._config.scopes])
        if "access_token" in result:
            self._access_token = result["access_token"]
        else:
            raise Exception("Failed to acquire token")
        return self._access_token

    @property
    def access_token(self):
        return self._access_token

    def msal_interactive_credentials(config) -> BaseCredentials:
        """Credentials for Azure using MSAL interactive"""
        client_id = config.get("core", CONFIG_CLIENT_ID)
        authority = config.get("core", CONFIG_AUTHENTICATION_AUTHORITY, None)
        scopes = config.get("core", CONFIG_AUTHENTICATION_SCOPES, None)
        cache_path = os.path.join(CLI_CONFIG_DIR, "msal_token_cache.bin")
        credentials = MsalInteractiveCredential(
            client_id, authority, scopes, cache_path
        )
        return credentials