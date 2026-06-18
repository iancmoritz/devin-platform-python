# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .daily import (
    DailyResource,
    AsyncDailyResource,
    DailyResourceWithRawResponse,
    AsyncDailyResourceWithRawResponse,
    DailyResourceWithStreamingResponse,
    AsyncDailyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConsumptionResource", "AsyncConsumptionResource"]


class ConsumptionResource(SyncAPIResource):
    @cached_property
    def daily(self) -> DailyResource:
        return DailyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return ConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return ConsumptionResourceWithStreamingResponse(self)


class AsyncConsumptionResource(AsyncAPIResource):
    @cached_property
    def daily(self) -> AsyncDailyResource:
        return AsyncDailyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConsumptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsumptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/iancmoritz/devin-platform-python#with_streaming_response
        """
        return AsyncConsumptionResourceWithStreamingResponse(self)


class ConsumptionResourceWithRawResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

    @cached_property
    def daily(self) -> DailyResourceWithRawResponse:
        return DailyResourceWithRawResponse(self._consumption.daily)


class AsyncConsumptionResourceWithRawResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

    @cached_property
    def daily(self) -> AsyncDailyResourceWithRawResponse:
        return AsyncDailyResourceWithRawResponse(self._consumption.daily)


class ConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: ConsumptionResource) -> None:
        self._consumption = consumption

    @cached_property
    def daily(self) -> DailyResourceWithStreamingResponse:
        return DailyResourceWithStreamingResponse(self._consumption.daily)


class AsyncConsumptionResourceWithStreamingResponse:
    def __init__(self, consumption: AsyncConsumptionResource) -> None:
        self._consumption = consumption

    @cached_property
    def daily(self) -> AsyncDailyResourceWithStreamingResponse:
        return AsyncDailyResourceWithStreamingResponse(self._consumption.daily)
