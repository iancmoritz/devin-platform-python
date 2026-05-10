# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FolderTree", "Folder"]


class Folder(BaseModel):
    """One folder in the knowledge folder tree."""

    folder_id: str

    name: str

    note_count: int

    path: str

    parent_folder_id: Optional[str] = None


class FolderTree(BaseModel):
    """Response for the folder-structure endpoint."""

    folders: List[Folder]

    root_note_count: int
