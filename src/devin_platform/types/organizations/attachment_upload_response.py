# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AttachmentUploadResponse"]


class AttachmentUploadResponse(BaseModel):
    attachment_id: str

    name: str

    url: str
