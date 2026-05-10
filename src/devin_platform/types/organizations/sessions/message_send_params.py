# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    org_id: Required[str]

    message: Required[str]

    message_as_user_id: Optional[str]
