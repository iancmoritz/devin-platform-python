# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["IdpGroupRegisterIdpGroupsParams"]


class IdpGroupRegisterIdpGroupsParams(TypedDict, total=False):
    idp_group_names: Required[SequenceNotStr[str]]
