# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    role_id: str

    role_name: str

    role_type: Literal["enterprise", "org"]
