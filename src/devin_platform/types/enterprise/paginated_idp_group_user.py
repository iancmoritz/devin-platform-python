# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .members.idp_role_assignment import IdpRoleAssignment

__all__ = ["PaginatedIdpGroupUser", "Item"]


class Item(BaseModel):
    """A user whose membership is derived from IDP group assignments."""

    email: Optional[str] = None

    idp_role_assignments: List[IdpRoleAssignment]

    name: Optional[str] = None

    user_id: str


class PaginatedIdpGroupUser(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
