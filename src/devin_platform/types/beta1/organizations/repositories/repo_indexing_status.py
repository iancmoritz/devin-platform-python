# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .repo_index_job import RepoIndexJob

__all__ = ["RepoIndexingStatus"]


class RepoIndexingStatus(BaseModel):
    indexing_enabled: bool

    latest_completed_search_index_job: Optional[RepoIndexJob] = None

    latest_completed_wiki_index_job: Optional[RepoIndexJob] = None

    latest_indexes: List[RepoIndexJob]
