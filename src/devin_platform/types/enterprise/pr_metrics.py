# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PrMetrics"]


class PrMetrics(BaseModel):
    """Response model for PR metrics."""

    prs_closed_count: int
    """PRs Devin authored that were closed without merging."""

    prs_created_count: int
    """Total PRs Devin authored across all states (open + merged + closed)."""

    prs_merged_count: int
    """PRs Devin authored that were merged."""

    prs_opened_count: int
    """PRs Devin authored that are currently open."""

    prs_taken_over_closed_count: Optional[int] = None
    """PRs Devin took over that were closed without merging."""

    prs_taken_over_count: Optional[int] = None
    """Total PRs Devin took over across all states (open + merged + closed).

    A take-over is when Devin pushed commits to a PR it did not originally create.
    """

    prs_taken_over_merged_count: Optional[int] = None
    """PRs Devin took over that were merged."""

    prs_taken_over_opened_count: Optional[int] = None
    """PRs Devin took over that are currently open."""
