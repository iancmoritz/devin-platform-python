# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionTerminateParams"]


class SessionTerminateParams(TypedDict, total=False):
    org_id: Required[str]

    archive: bool
    """Whether to archive the devin session"""
