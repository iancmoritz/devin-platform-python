# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["NoteListParams"]


class NoteListParams(TypedDict, total=False):
    access_type: Optional[Literal["org", "enterprise"]]

    after: Optional[str]

    first: int

    folder_path: Optional[str]

    pinned_repo: Optional[str]

    search: Optional[str]
