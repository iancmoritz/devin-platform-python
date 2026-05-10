# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .session_pull_request import SessionPullRequest

__all__ = ["SessionResponse"]


class SessionResponse(BaseModel):
    acus_consumed: float

    created_at: int

    org_id: str

    pull_requests: List[SessionPullRequest]

    session_id: str

    status: Literal["new", "claimed", "running", "exit", "error", "suspended", "resuming"]

    tags: List[str]

    updated_at: int

    url: str

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
    ] = None
    """The session's assigned use-case category, if categorisation has run.

    Only populated on get/list endpoints.
    """

    child_session_ids: Optional[List[str]] = None

    is_archived: Optional[bool] = None

    origin: Optional[
        Literal["webapp", "slack", "teams", "api", "linear", "jira", "automation", "cli", "desktop", "other"]
    ] = None
    """The origin from which the session was created."""

    parent_session_id: Optional[str] = None

    playbook_id: Optional[str] = None

    service_user_id: Optional[str] = None

    status_detail: Optional[
        Literal[
            "working",
            "waiting_for_user",
            "waiting_for_approval",
            "finished",
            "inactivity",
            "user_request",
            "usage_limit_exceeded",
            "out_of_credits",
            "out_of_quota",
            "no_quota_allocation",
            "payment_declined",
            "org_usage_limit_exceeded",
            "total_session_limit_exceeded",
            "error",
        ]
    ] = None
    """Additional detail about the session's current status.

    When status is 'running': 'working' (actively working), 'waiting_for_user'
    (needs user input), 'waiting_for_approval' (awaiting action approval in safe
    mode), or 'finished' (task complete). When status is 'suspended': the reason for
    suspension such as 'inactivity', 'user_request', 'usage_limit_exceeded',
    'out_of_credits', 'out_of_quota', 'no_quota_allocation', 'payment_declined',
    'org_usage_limit_exceeded', 'total_session_limit_exceeded', or 'error'. Only
    populated on get/list endpoints.
    """

    structured_output: Optional[Dict[str, object]] = None
    """Validated structured output from the session.

    Only populated on get/list endpoints.
    """

    subcategory: Optional[str] = None
    """The session's assigned subcategory display name.

    'Other' when a category is set but no subcategory was assigned or resolved. Only
    populated on get/list endpoints.
    """

    title: Optional[str] = None

    user_id: Optional[str] = None
