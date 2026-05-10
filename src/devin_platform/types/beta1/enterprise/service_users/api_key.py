# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """
    Shared response model for API key details (used by both PAT and service user endpoints).
    """

    api_key_id: str

    api_key_name: str

    created_at: int

    expires_at: Optional[int] = None

    is_active: bool

    last_used_at: Optional[int] = None

    revoked_at: Optional[int] = None
