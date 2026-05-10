# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["SessionInsightsNoteUsageItem"]


class SessionInsightsNoteUsageItem(BaseModel):
    message: str

    note_id: str

    reason: str
