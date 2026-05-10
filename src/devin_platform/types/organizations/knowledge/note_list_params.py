# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NoteListParams"]


class NoteListParams(TypedDict, total=False):
    after: Optional[str]

    first: int

    folder_path: Optional[str]

    pinned_repo: Optional[str]

    search: Optional[str]
