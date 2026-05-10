# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageListParams", "Qs"]


class MessageListParams(TypedDict, total=False):
    qs: Required[Qs]

    org_id: Optional[str]


class Qs(TypedDict, total=False):
    after: Optional[str]

    first: int
