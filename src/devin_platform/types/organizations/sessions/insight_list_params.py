# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["InsightListParams", "Qs"]


class InsightListParams(TypedDict, total=False):
    qs: Required[Qs]

    devin_id: Optional[str]


class Qs(TypedDict, total=False):
    after: Optional[str]

    category: Optional[
        Literal[
            "bug_fixing",
            "ci_cd_and_devops",
            "code_quality_and_security",
            "code_review_and_analysis",
            "data_and_automation",
            "documentation_and_content",
            "feature_development",
            "migrations_and_upgrades",
            "other",
            "refactoring_and_optimization",
            "research_and_exploration",
            "unit_test_generation",
        ]
    ]

    created_after: Optional[int]

    created_before: Optional[int]

    first: int

    is_archived: Optional[bool]

    origins: Optional[
        List[Literal["webapp", "slack", "teams", "api", "linear", "jira", "automation", "cli", "desktop", "other"]]
    ]

    playbook_id: Optional[str]

    repo_names: Optional[SequenceNotStr[str]]
    """Filter by repository names (e.g., 'owner/repo')"""

    schedule_id: Optional[str]

    service_user_ids: Optional[SequenceNotStr[str]]

    session_ids: Optional[SequenceNotStr[str]]

    tags: Optional[SequenceNotStr[str]]

    updated_after: Optional[int]

    updated_before: Optional[int]

    user_ids: Optional[SequenceNotStr[str]]
