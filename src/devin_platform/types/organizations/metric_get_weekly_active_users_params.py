# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetricGetWeeklyActiveUsersParams"]


class MetricGetWeeklyActiveUsersParams(TypedDict, total=False):
    time_after: Required[int]

    time_before: Required[int]

    min_searches: int

    min_sessions: int
