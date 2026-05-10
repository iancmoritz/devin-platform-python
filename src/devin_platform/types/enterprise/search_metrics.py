# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SearchMetrics"]


class SearchMetrics(BaseModel):
    """Response model for search metrics."""

    searches_created_count: int
