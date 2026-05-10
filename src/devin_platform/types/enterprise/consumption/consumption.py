# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["Consumption", "ConsumptionByDate", "ConsumptionByDateAcusByProduct"]


class ConsumptionByDateAcusByProduct(BaseModel):
    cascade: float

    devin: float

    terminal: float


class ConsumptionByDate(BaseModel):
    acus: float

    acus_by_product: ConsumptionByDateAcusByProduct

    date: int


class Consumption(BaseModel):
    consumption_by_date: List[ConsumptionByDate]

    total_acus: float
