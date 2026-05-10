# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MetricGetSessionMetricsParams"]


class MetricGetSessionMetricsParams(TypedDict, total=False):
    time_after: Required[int]

    time_before: Required[int]

    playbook_id: Optional[str]

    service_user_ids: Optional[SequenceNotStr[str]]

    user_ids: Optional[SequenceNotStr[str]]
