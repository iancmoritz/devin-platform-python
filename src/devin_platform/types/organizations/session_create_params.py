# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SessionCreateParams", "SessionSecret"]


class SessionCreateParams(TypedDict, total=False):
    prompt: Required[str]

    advanced_mode: Optional[Literal["analyze", "create", "improve", "batch", "manage"]]

    attachment_urls: Optional[SequenceNotStr[str]]

    bypass_approval: Optional[bool]

    child_playbook_id: Optional[str]

    create_as_user_id: Optional[str]

    knowledge_ids: Optional[SequenceNotStr[str]]

    max_acu_limit: Optional[int]

    playbook_id: Optional[str]

    repos: Optional[SequenceNotStr[str]]

    secret_ids: Optional[SequenceNotStr[str]]

    session_links: Optional[SequenceNotStr[str]]

    session_secrets: Optional[Iterable[SessionSecret]]

    structured_output_schema: Optional[Dict[str, object]]
    """JSON Schema (Draft 7) for validating structured output.

    Max 64KB. Must be self-contained (no external $ref).
    """

    tags: Optional[SequenceNotStr[str]]

    title: Optional[str]


class SessionSecret(TypedDict, total=False):
    """Input model for a session secret provided via API."""

    key: Required[str]

    value: Required[str]

    sensitive: bool
