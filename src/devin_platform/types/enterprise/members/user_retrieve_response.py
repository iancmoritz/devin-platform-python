# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .role_assignment import RoleAssignment
from .idp_role_assignment import IdpRoleAssignment

__all__ = ["UserRetrieveResponse"]


class UserRetrieveResponse(BaseModel):
    """User with both direct and IDP-group-derived role assignments."""

    email: Optional[str] = None

    name: Optional[str] = None

    role_assignments: List[RoleAssignment]

    user_id: str

    idp_role_assignments: Optional[List[IdpRoleAssignment]] = None
