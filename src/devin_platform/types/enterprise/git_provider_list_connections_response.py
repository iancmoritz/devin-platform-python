# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GitProviderListConnectionsResponse", "Item"]


class Item(BaseModel):
    created_at: int

    git_connection_id: str

    git_provider_type: Literal[
        "github_token",
        "github_individual_token",
        "github_app",
        "gitlab_token",
        "gitlab_oauth",
        "azure_devops_oauth",
        "bitbucket_oauth",
        "bitbucket_token",
    ]

    host: str

    name: Optional[str] = None


class GitProviderListConnectionsResponse(BaseModel):
    items: List[Item]

    end_cursor: Optional[str] = None
    """Cursor to fetch the next page, or None if this is the last page."""

    has_next_page: Optional[bool] = None
    """Whether there are more items available after this page."""

    total: Optional[int] = None
    """Optional total count (can be omitted for performance)."""
