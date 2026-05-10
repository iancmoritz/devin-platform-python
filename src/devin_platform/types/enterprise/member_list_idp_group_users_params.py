# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemberListIdpGroupUsersParams"]


class MemberListIdpGroupUsersParams(TypedDict, total=False):
    after: Optional[str]

    email: Optional[str]
    """Filter by exact email address"""

    first: int
