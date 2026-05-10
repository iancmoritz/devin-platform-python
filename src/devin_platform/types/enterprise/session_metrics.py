# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .session_counts_by_size import SessionCountsBySize

__all__ = ["SessionMetrics", "SessionsCreatedByOrigin"]


class SessionsCreatedByOrigin(BaseModel):
    """Session counts by origin type.

    Note: The internal analytics model tracks additional origins (cli, vscode_extension,
    devin_spaces) that are not exposed in this API model. Sessions from those origins
    are not included in the API response.
    """

    api: Optional[int] = None

    jira: Optional[int] = None

    linear: Optional[int] = None

    slack: Optional[int] = None

    teams: Optional[int] = None

    webapp: Optional[int] = None


class SessionMetrics(BaseModel):
    """Response model for session metrics."""

    avg_acus_per_session: float

    sessions_created_by_origin: SessionsCreatedByOrigin
    """Session counts by origin type.

    Note: The internal analytics model tracks additional origins (cli,
    vscode_extension, devin_spaces) that are not exposed in this API model. Sessions
    from those origins are not included in the API response.
    """

    sessions_created_by_size: SessionCountsBySize
    """Session counts by size category."""

    sessions_created_count: int

    sessions_created_with_playbook_count: int

    sessions_created_with_search_count: int

    sessions_with_merged_prs_by_size: SessionCountsBySize
    """Session counts by size category."""

    sessions_with_merged_prs_count: int
