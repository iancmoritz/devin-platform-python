# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["OrgGroupsConfig", "Groups"]


class Groups(BaseModel):
    org_ids: List[str]

    max_cycle_acus: Optional[int] = None


class OrgGroupsConfig(BaseModel):
    """Configuration mapping group names to their settings."""

    groups: Dict[str, Groups]
