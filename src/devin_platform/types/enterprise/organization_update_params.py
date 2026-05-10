# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    max_cycle_acu_limit: Optional[int]

    max_session_acu_limit: Optional[int]

    name: Optional[str]
