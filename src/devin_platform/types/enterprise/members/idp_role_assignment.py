# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...role import Role
from ...._models import BaseModel

__all__ = ["IdpRoleAssignment"]


class IdpRoleAssignment(BaseModel):
    """A role assignment inherited via IDP group membership."""

    idp_group_name: str

    role: Role

    org_id: Optional[str] = None
