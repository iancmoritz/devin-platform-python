# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .knowledge_note import KnowledgeNote

__all__ = ["PaginatedKnowledgeNoteResponse"]


class PaginatedKnowledgeNoteResponse(BaseModel):
    items: List[KnowledgeNote]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
