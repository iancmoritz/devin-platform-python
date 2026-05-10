# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PermissionCreateParams", "Permission"]


class PermissionCreateParams(TypedDict, total=False):
    permissions: Required[Iterable[Permission]]


class Permission(TypedDict, total=False):
    git_connection_id: Required[str]

    group_prefix: Optional[str]

    prefix_path: Optional[str]

    repo_path: Optional[str]
