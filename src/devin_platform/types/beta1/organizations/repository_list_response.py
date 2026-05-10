# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .repositories.repo_indexing_status import RepoIndexingStatus

__all__ = ["RepositoryListResponse", "Item"]


class Item(BaseModel):
    git_connection_host: str

    git_connection_id: str

    indexing_status: Optional[RepoIndexingStatus] = None

    last_updated_at: Optional[int] = None

    provider_repository_id: str

    repo_description: Optional[str] = None

    repo_language: Optional[str] = None

    repo_name: str

    repo_path: str


class RepositoryListResponse(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
