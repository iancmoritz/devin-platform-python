# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EnterpriseGetQueueStatusResponse"]


class EnterpriseGetQueueStatusResponse(BaseModel):
    """Response model for queue endpoint."""

    queue_size: int

    status: Literal["normal", "elevated", "high"]
