# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    created_at: int

    max_cycle_acu_limit: Optional[int] = None

    max_session_acu_limit: Optional[int] = None

    name: str

    org_id: str

    updated_at: int
