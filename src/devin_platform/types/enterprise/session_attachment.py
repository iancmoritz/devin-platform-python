# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SessionAttachment"]


class SessionAttachment(BaseModel):
    """An attachment sent during a session."""

    attachment_id: str

    name: str

    source: Literal["devin", "user"]

    url: str

    content_type: Optional[str] = None
