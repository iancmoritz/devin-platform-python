# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["GitPermission"]


class GitPermission(BaseModel):
    git_connection_id: str

    git_permission_id: str

    created_at: Optional[int] = None

    group_prefix: Optional[str] = None

    prefix_path: Optional[str] = None

    read_only: Optional[bool] = None

    repo_path: Optional[str] = None
