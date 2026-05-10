# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EnterpriseListHypervisorsResponse", "Item"]


class Item(BaseModel):
    cloud_provider_instance_id: Optional[str] = None

    created_at: Optional[int] = None

    hypervisor_id: str

    last_heartbeat: Optional[int] = None

    status: str

    utilization_percentage: float


class EnterpriseListHypervisorsResponse(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
