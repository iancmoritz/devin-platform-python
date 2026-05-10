# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .role_assignment import RoleAssignment

__all__ = ["ServiceUser"]


class ServiceUser(BaseModel):
    expires_at: Optional[int] = None

    name: str

    role_assignments: List[RoleAssignment]

    service_user_id: str
