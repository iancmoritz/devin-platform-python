# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..enterprise.session_attachment import SessionAttachment

__all__ = ["SessionListAttachmentsResponse"]

SessionListAttachmentsResponse: TypeAlias = List[SessionAttachment]
