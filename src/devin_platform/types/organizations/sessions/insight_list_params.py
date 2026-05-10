# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["InsightListParams"]


class InsightListParams(TypedDict, total=False):
    after: Optional[str]

    created_after: Optional[int]

    created_before: Optional[int]

    first: int

    origins: Optional[List[Literal["webapp", "slack", "teams", "api", "linear", "jira", "scheduled", "cli", "other"]]]

    playbook_id: Optional[str]

    schedule_id: Optional[str]

    service_user_ids: Optional[SequenceNotStr[str]]

    session_ids: Optional[SequenceNotStr[str]]

    tags: Optional[SequenceNotStr[str]]

    updated_after: Optional[int]

    updated_before: Optional[int]

    user_ids: Optional[SequenceNotStr[str]]
