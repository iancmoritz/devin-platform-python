# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    access_type: Literal["org", "personal"]

    created_at: int

    created_by: str

    is_sensitive: bool

    key: Optional[str] = None

    note: Optional[str] = None

    secret_id: str

    secret_type: Literal["cookie", "key-value", "totp"]

    updated_at: Optional[int] = None

    updated_by: Optional[str] = None
