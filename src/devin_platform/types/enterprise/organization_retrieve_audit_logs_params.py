# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..audit_log_action import AuditLogAction

__all__ = ["OrganizationRetrieveAuditLogsParams"]


class OrganizationRetrieveAuditLogsParams(TypedDict, total=False):
    action: Optional[AuditLogAction]

    after: Optional[str]

    first: int

    order: Literal["asc", "desc"]

    time_after: Optional[int]

    time_before: Optional[int]
