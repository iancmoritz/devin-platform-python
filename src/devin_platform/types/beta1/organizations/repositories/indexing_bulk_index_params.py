# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["IndexingBulkIndexParams", "Repository"]


class IndexingBulkIndexParams(TypedDict, total=False):
    repositories: Required[Iterable[Repository]]


class Repository(TypedDict, total=False):
    repository_path: Required[str]
    """e.g., 'org/repo-name'"""

    branch_names: SequenceNotStr[str]
