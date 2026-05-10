# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ActiveUserMetrics"]


class ActiveUserMetrics(BaseModel):
    """Single entry for active users over time."""

    active_users: int

    end_time: int

    start_time: int
