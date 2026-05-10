# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UsageMetrics"]


class UsageMetrics(BaseModel):
    prs_created_count: int

    prs_merged_count: int

    searches_count: int

    sessions_count: int
