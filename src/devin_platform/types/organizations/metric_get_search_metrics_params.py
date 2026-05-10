# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetricGetSearchMetricsParams"]


class MetricGetSearchMetricsParams(TypedDict, total=False):
    time_after: Required[int]

    time_before: Required[int]
