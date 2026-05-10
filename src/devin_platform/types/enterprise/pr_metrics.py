# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PrMetrics"]


class PrMetrics(BaseModel):
    """Response model for PR metrics."""

    prs_closed_count: int

    prs_created_count: int

    prs_merged_count: int

    prs_opened_count: int
