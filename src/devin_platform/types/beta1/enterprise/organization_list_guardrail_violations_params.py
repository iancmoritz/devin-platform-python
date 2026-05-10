# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["OrganizationListGuardrailViolationsParams"]


class OrganizationListGuardrailViolationsParams(TypedDict, total=False):
    after: Optional[str]

    first: int

    guardrail_id: Optional[str]

    order: Literal["asc", "desc"]

    session_id: Optional[str]

    time_after: Optional[int]

    time_before: Optional[int]
