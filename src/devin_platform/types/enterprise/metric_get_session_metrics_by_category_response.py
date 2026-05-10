# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MetricGetSessionMetricsByCategoryResponse", "Category", "CategorySubcategory"]


class CategorySubcategory(BaseModel):
    acus: float

    display_name: str

    sessions_count: int

    subcategory_id: Optional[str] = None


class Category(BaseModel):
    acus: float

    category: str

    sessions_count: int

    subcategories: List[CategorySubcategory]


class MetricGetSessionMetricsByCategoryResponse(BaseModel):
    categories: List[Category]
