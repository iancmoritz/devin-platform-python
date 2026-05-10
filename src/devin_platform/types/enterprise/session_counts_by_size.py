# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SessionCountsBySize"]


class SessionCountsBySize(BaseModel):
    """Session counts by size category."""

    l: Optional[int] = None

    m: Optional[int] = None

    s: Optional[int] = None

    xl: Optional[int] = None

    xs: Optional[int] = None
