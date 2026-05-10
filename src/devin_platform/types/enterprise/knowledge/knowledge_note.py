# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["KnowledgeNote"]


class KnowledgeNote(BaseModel):
    access_type: Literal["enterprise", "org"]

    body: str

    created_at: int

    folder_id: Optional[str] = None

    folder_path: str

    is_enabled: bool

    macro: Optional[str] = None

    name: str

    note_id: str

    org_id: Optional[str] = None

    pinned_repo: Optional[str] = None

    trigger: str

    updated_at: int
