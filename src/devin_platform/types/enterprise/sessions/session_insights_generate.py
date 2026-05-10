# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["SessionInsightsGenerate"]


class SessionInsightsGenerate(BaseModel):
    """Response from triggering session insights generation."""

    session_id: str
    """The session ID for which insights generation was triggered."""

    status: str
    """The status of the generation request."""
