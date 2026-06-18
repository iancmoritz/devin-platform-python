# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    agent: Optional[Literal["devin", "data_analyst"]]

    bypass_approval: Optional[bool]

    enabled: Optional[bool]

    frequency: Optional[str]

    interval_count: Optional[int]

    name: Optional[str]

    notify_on: Optional[Literal["always", "failure", "never"]]

    playbook_id: Optional[str]

    prompt: Optional[str]

    run_as_user_id: Optional[str]
    """Set the user ID that this schedule will run as.

    Requires ImpersonateOrgSessions permission. Setting to null reverts to the
    default bot user. Omitting the field leaves the current identity unchanged.
    """

    schedule_type: Optional[Literal["recurring", "one_time"]]

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    slack_channel_id: Optional[str]

    slack_team_id: Optional[str]

    tags: Optional[SequenceNotStr[str]]

    target_devin_id: Optional[str]
