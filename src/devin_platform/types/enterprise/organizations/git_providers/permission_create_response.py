# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .git_permission import GitPermission

__all__ = ["PermissionCreateResponse"]

PermissionCreateResponse: TypeAlias = List[GitPermission]
