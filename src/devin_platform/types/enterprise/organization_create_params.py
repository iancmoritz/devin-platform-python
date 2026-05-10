# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]

    max_cycle_acu_limit: Optional[int]

    max_session_acu_limit: Optional[int]
