# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionPullRequest"]


class SessionPullRequest(BaseModel):
    pr_state: Optional[str] = None

    pr_url: str
