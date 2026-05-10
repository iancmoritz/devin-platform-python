# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PlaybookResponse"]


class PlaybookResponse(BaseModel):
    access_type: Literal["enterprise", "org"]

    body: str

    created_at: int

    created_by: str

    macro: Optional[str] = None

    org_id: Optional[str] = None

    playbook_id: str

    title: str

    updated_at: int

    updated_by: str
