# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .repository_indexing import RepositoryIndexing

__all__ = ["IndexingBulkIndexResponse"]

IndexingBulkIndexResponse: TypeAlias = List[RepositoryIndexing]
