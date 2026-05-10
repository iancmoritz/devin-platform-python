# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ScheduleCreateParams"]


class ScheduleCreateParams(TypedDict, total=False):
    name: Required[str]

    prompt: Required[str]

    agent: Literal["devin", "data_analyst"]

    bypass_approval: bool

    create_as_user_id: Optional[str]

    frequency: Optional[str]

    interval_count: int

    notify_on: Literal["always", "failure", "never"]

    playbook_id: Optional[str]

    schedule_type: Literal["recurring", "one_time"]

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    slack_channel_id: Optional[str]

    slack_team_id: Optional[str]

    tags: Optional[SequenceNotStr[str]]

    target_devin_id: Optional[str]
