# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MetricGetMonthlyActiveUsersParams"]


class MetricGetMonthlyActiveUsersParams(TypedDict, total=False):
    time_after: Required[int]

    time_before: Required[int]

    min_searches: int

    min_sessions: int

    org_ids: Optional[SequenceNotStr[str]]
