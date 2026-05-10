# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]

    expires_at: Optional[int]
    """Optional expiration as a UNIX timestamp in seconds.

    Must be in the future if provided.
    """
