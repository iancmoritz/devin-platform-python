# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PlaybookUpdateParams"]


class PlaybookUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    body: Required[str]

    title: Required[str]

    macro: Optional[str]
    """Playbook macro identifier.

    Must start with '!' followed by one or more letters, digits, underscores, or
    hyphens. Example: '!my_macro' or '!my-macro'
    """
