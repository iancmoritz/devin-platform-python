# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .session_attachment import SessionAttachment

__all__ = ["SessionRetrieveAttachmentsResponse"]

SessionRetrieveAttachmentsResponse: TypeAlias = List[SessionAttachment]
