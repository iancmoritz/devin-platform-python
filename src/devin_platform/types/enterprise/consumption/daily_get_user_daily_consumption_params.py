# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DailyGetUserDailyConsumptionParams"]


class DailyGetUserDailyConsumptionParams(TypedDict, total=False):
    time_after: Optional[int]

    time_before: Optional[int]
