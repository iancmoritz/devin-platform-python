# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..enterprise.active_user_metrics import ActiveUserMetrics

__all__ = ["MetricGetMonthlyActiveUsersResponse"]

MetricGetMonthlyActiveUsersResponse: TypeAlias = List[ActiveUserMetrics]
