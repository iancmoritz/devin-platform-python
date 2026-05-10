# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    message: Required[str]

    org_id: Optional[str]

    message_as_user_id: Optional[str]
