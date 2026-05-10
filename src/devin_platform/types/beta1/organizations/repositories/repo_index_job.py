# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RepoIndexJob"]


class RepoIndexJob(BaseModel):
    branch_name: Optional[str] = None

    commit: str

    created_at: int

    job_id: str

    status: Literal["failed", "completed", "in_progress"]
