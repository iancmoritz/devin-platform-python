# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .role_assignment import RoleAssignment

__all__ = ["User"]


class User(BaseModel):
    email: Optional[str] = None

    name: Optional[str] = None

    role_assignments: List[RoleAssignment]

    user_id: str
