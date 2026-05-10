# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Schedule", "Playbook"]


class Playbook(BaseModel):
    playbook_id: str

    title: Optional[str] = None


class Schedule(BaseModel):
    agent: Literal["devin", "data_analyst", "advanced"]

    consecutive_failures: int

    created_at: datetime

    created_by: Optional[str] = None

    enabled: bool

    frequency: Optional[str] = None

    last_error_at: Optional[datetime] = None

    last_error_message: Optional[str] = None

    last_executed_at: Optional[datetime] = None

    name: str

    notify_on: Literal["always", "failure", "never"]

    org_id: str

    playbook: Optional[Playbook] = None

    prompt: str

    scheduled_session_id: str

    updated_at: datetime

    bypass_approval: Optional[bool] = None

    interval_count: Optional[int] = None

    schedule_type: Optional[Literal["recurring", "one_time"]] = None

    scheduled_at: Optional[datetime] = None

    slack_channel_id: Optional[str] = None

    slack_team_id: Optional[str] = None

    tags: Optional[List[str]] = None

    target_devin_id: Optional[str] = None
