# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["APIKeyWithToken"]


class APIKeyWithToken(BaseModel):
    """Shared response model for API key creation/rotation (includes one-time token)."""

    token: str
    """The raw API token. This is only shown once at creation/rotation time."""

    api_key_id: str

    api_key_name: str
