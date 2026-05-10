# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["RepositoryListParams"]


class RepositoryListParams(TypedDict, total=False):
    after: Optional[str]

    exclude_repo_paths: Optional[SequenceNotStr[str]]

    filter_name: Optional[str]

    first: int

    load_indexing_status: bool

    only_repo_paths: Optional[SequenceNotStr[str]]
