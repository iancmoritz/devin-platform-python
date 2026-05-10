# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["cookie", "key-value", "totp"]]

    value: Required[str]

    is_sensitive: bool

    note: Optional[str]
