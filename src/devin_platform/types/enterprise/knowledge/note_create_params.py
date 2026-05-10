# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["NoteCreateParams"]


class NoteCreateParams(TypedDict, total=False):
    body: Required[str]

    name: Required[str]

    trigger: Required[str]

    folder_id: Optional[str]

    is_enabled: Optional[bool]

    pinned_repo: Optional[str]
