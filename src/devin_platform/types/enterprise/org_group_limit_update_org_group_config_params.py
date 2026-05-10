# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OrgGroupLimitUpdateOrgGroupConfigParams", "Groups"]


class OrgGroupLimitUpdateOrgGroupConfigParams(TypedDict, total=False):
    groups: Required[Dict[str, Groups]]


class Groups(TypedDict, total=False):
    org_ids: Required[SequenceNotStr[str]]

    max_cycle_acus: Optional[int]
