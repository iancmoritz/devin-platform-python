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

    status: Literal["new", "creating", "claimed", "running", "exit", "error", "suspended", "resuming"]

    tags: List[str]

    updated_at: int

    url: str

    child_session_ids: Optional[List[str]] = None

    is_advanced: Optional[bool] = None

    is_archived: Optional[bool] = None

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
            "error",
        ]
    ] = None
    """Additional detail about the session's current status.

    When status is 'running': 'working' (actively working), 'waiting_for_user'
    (needs user input), 'waiting_for_approval' (awaiting action approval in safe
    mode), or 'finished' (task complete). When status is 'suspended': the reason for
    suspension such as 'inactivity', 'user_request', 'usage_limit_exceeded',
    'out_of_credits', 'out_of_quota', 'no_quota_allocation', 'payment_declined',
    'org_usage_limit_exceeded', or 'error'. Only populated on get/list endpoints.
    """

    structured_output: Optional[Dict[str, object]] = None
    """Validated structured output from the session.

    Only populated on get/list endpoints.
    """

    title: Optional[str] = None

    user_id: Optional[str] = None
