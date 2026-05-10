# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SessionCreateParams", "SessionSecret"]


class SessionCreateParams(TypedDict, total=False):
    prompt: Required[str]

    devin_id: Optional[str]

    attachment_urls: Optional[SequenceNotStr[str]]

    bypass_approval: Optional[bool]

    child_playbook_id: Optional[str]

    create_as_user_id: Optional[str]

    knowledge_ids: Optional[SequenceNotStr[str]]

    max_acu_limit: Optional[int]

    platform: Optional[str]
    """Override the VM platform for the session (e.g.

    'windows'). When omitted (or set to 'inherit'), a session created by a parent
    Devin inherits the parent's platform; otherwise the organization default is
    used. Pass 'default' to force the organization default regardless of parent. Any
    other value must match a platform configured for your organization
    (case-insensitive); unrecognized values are rejected with a 400 whose error body
    lists the available platform labels for the org.
    """

    playbook_id: Optional[str]

    repos: Optional[SequenceNotStr[str]]

    secret_ids: Optional[SequenceNotStr[str]]

    session_links: Optional[SequenceNotStr[str]]

    session_secrets: Optional[Iterable[SessionSecret]]

    structured_output_required: Optional[bool]
    """
    When true (default), the agent MUST call provide_structured_output with
    is_final=true before its turn ends. When false, the tool is available but not
    required — it is not guaranteed to be called in a given turn.
    """

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
