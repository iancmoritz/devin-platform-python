# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PaginatedResponse", "Item"]


class Item(BaseModel):
    action_taken: str

    confidence_score: float

    created_at: int

    event_id: str

    guardrail_id: str

    guardrail_name: str

    org_id: str

    reasoning: str

    session_id: Optional[str] = None

    user_message: str

    violation_id: int


class PaginatedResponse(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
