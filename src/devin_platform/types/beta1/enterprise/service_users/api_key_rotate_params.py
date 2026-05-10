# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["APIKeyRotateParams"]


class APIKeyRotateParams(TypedDict, total=False):
    service_user_id: Required[str]

    new_key_expires_at: Optional[int]
    """Optional expiration for the new key as a UNIX timestamp in seconds.

    Null for no expiration.
    """

    revoke_current: bool
    """Whether to revoke the current key. Set to False for graceful rollover."""
