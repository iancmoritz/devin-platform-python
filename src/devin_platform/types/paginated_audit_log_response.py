# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .audit_log_action import AuditLogAction

__all__ = ["PaginatedAuditLogResponse", "Item"]


class Item(BaseModel):
    action: AuditLogAction

    audit_log_id: str

    created_at: int

    data: Dict[str, object]

    org_id: Optional[str] = None

    service_user_id: Optional[str] = None

    service_user_name: Optional[str] = None

    user_email: Optional[str] = None

    user_id: Optional[str] = None


class PaginatedAuditLogResponse(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
