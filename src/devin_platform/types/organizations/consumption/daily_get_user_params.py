# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DailyGetUserParams"]


class DailyGetUserParams(TypedDict, total=False):
    org_id: Required[str]

    time_after: Optional[int]

    time_before: Optional[int]
