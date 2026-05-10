# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .repo_indexing_status import RepoIndexingStatus

__all__ = ["RepositoryIndexing"]


class RepositoryIndexing(BaseModel):
    branches: List[str]

    indexing_enabled: bool

    repository_path: str

    indexing_status: Optional[RepoIndexingStatus] = None
