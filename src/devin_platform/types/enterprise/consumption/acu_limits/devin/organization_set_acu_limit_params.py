# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationSetAcuLimitParams"]


class OrganizationSetAcuLimitParams(TypedDict, total=False):
    cycle_acu_limit: Required[int]
