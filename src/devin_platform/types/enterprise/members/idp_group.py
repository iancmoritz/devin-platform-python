# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .role_assignment import RoleAssignment

__all__ = ["IdpGroup"]


class IdpGroup(BaseModel):
    idp_group_name: str

    role_assignments: List[RoleAssignment]
